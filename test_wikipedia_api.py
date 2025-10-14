import argparse
import datetime as dt
import csv
import urllib.parse
import requests
import sys

REST = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
PROJECT = "en.wikipedia.org"
ACCESS = "all-access"   # desktop + mobile combined
AGENT = "user"          # excludes bots
GRAN = "daily"

def yyyymmdd(d: dt.date) -> str:
    return d.strftime("%Y%m%d")

def last_30_full_days(today=None):
    if today is None:
        today = dt.date.today()
    end = today - dt.timedelta(days=1)       # yesterday = last complete day
    start = end - dt.timedelta(days=29)      # 30 days total
    return start, end

def fetch_pageviews(title: str, start: dt.date, end: dt.date):
    safe = urllib.parse.quote(title.replace(" ", "_"), safe="")
    url = f"{REST}/{PROJECT}/{ACCESS}/{AGENT}/{safe}/{GRAN}/{yyyymmdd(start)}/{yyyymmdd(end)}"
    try:
        r = requests.get(url, timeout=20)
        if r.status_code != 200:
            return []
        items = r.json().get("items", [])
        return [int(it.get("views", 0)) for it in items]
    except requests.RequestException:
        return []

def summarize(title: str, views):
    days = len(views)
    total = sum(views)
    avg = round(total / days, 2) if days else 0.0
    return {"title": title, "days": days, "total": total, "avg_per_day": avg}

def print_table(rows, start, end):
    if not rows:
        print("No results.")
        return
    print(f"# Wikipedia Attention — {start} to {end}\n")
    header = ["Title", "Days", "Total Views", "Avg/Day"]
    keys = ["title","days","total","avg_per_day"]
    widths = [max(len(str(r[k])) for r in rows + [{k: h}]) for k, h in zip(keys, header)]
    print(f"{header[0]:<{widths[0]}}  {header[1]:>{widths[1]}}  {header[2]:>{widths[2]}}  {header[3]:>{widths[3]}}")
    print("-" * (sum(widths) + 6))
    for r in rows:
        print(f"{r['title']:<{widths[0]}}  {r['days']:>{widths[1]}}  {r['total']:>{widths[2]}}  {r['avg_per_day']:>{widths[3]}}")

def write_csv(rows, path="results_week7.csv"):
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["title","days","total","avg_per_day"])
        w.writeheader()
        w.writerows(rows)

def parse_args():
    p = argparse.ArgumentParser(description="Compare Wikipedia topics by average daily pageviews over a date window (default: last 30 full days).")
    p.add_argument("titles", nargs="+", help="Wikipedia page titles (e.g., 'Machine learning' 'Deep learning')")
    p.add_argument("--start", type=str, help="Start date YYYY-MM-DD (optional)")
    p.add_argument("--end", type=str, help="End date YYYY-MM-DD (optional)")
    return p.parse_args()

def main():
    args = parse_args()
    if args.start and args.end:
        try:
            start = dt.date.fromisoformat(args.start)
            end = dt.date.fromisoformat(args.end)
        except ValueError:
            print("ERROR: --start/--end must be YYYY-MM-DD", file=sys.stderr)
            sys.exit(1)
    else:
        start, end = last_30_full_days()

    results = []
    for t in args.titles:
        views = fetch_pageviews(t, start, end)
        results.append(summarize(t, views))

    # Rank by sustained attention
    results.sort(key=lambda r: r["avg_per_day"], reverse=True)

    print_table(results, start, end)
    write_csv(results)
    print("\nSaved: results_week7.csv")

if __name__ == "__main__":
    main()
