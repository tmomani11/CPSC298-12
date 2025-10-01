import requests
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

WIKI_API = "https://en.wikipedia.org/w/api.php"

def fetch_revisions(title, limit=50):

    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "titles": title,
        "rvprop": "user|timestamp|comment",
        "rvlimit": limit
    }
    headers = {
        "User-Agent": "WikiProjectBot/1.0 (tylermomani@chapman.edu)"
    }
    response = requests.get(WIKI_API, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    return page.get("revisions", [])

def analyze_revisions(revisions):

    users = [rev.get("user", "Unknown") for rev in revisions]
    user_counts = Counter(users)

    print("\n=== Revision Stats ===")
    print(f"Total revisions analyzed: {len(revisions)}")
    print(f"Unique contributors: {len(user_counts)}")

    print("\nTop contributors:")
    for user, count in user_counts.most_common(5):
        print(f"- {user}: {count} edits")

    timestamps = [rev["timestamp"] for rev in revisions]
    if timestamps:
        first_edit = datetime.fromisoformat(timestamps[-1].replace("Z", "+00:00"))
        last_edit = datetime.fromisoformat(timestamps[0].replace("Z", "+00:00"))
        print(f"\nFirst edit in this batch: {first_edit}")
        print(f"Most recent edit: {last_edit}")

    return user_counts, timestamps


def plot_top_contributors(user_counts, top_n=10):

    top_users = user_counts.most_common(top_n)
    users, counts = zip(*top_users)

    plt.figure(figsize=(10, 5))
    plt.bar(users, counts)
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Top {top_n} Contributors")
    plt.xlabel("User")
    plt.ylabel("Number of Edits")
    plt.tight_layout()
    plt.show()


def plot_edits_over_time(timestamps):

    dates = [datetime.fromisoformat(ts.replace("Z", "+00:00")).date() for ts in timestamps]
    date_counts = Counter(dates)
    sorted_dates = sorted(date_counts.items())

    days, counts = zip(*sorted_dates)

    plt.figure(figsize=(10, 5))
    plt.plot(days, counts, marker="o")
    plt.title("Edits Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Edits")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def print_revision_details(revisions, num=5):

    print(f"\n=== Last {num} Revisions ===")
    for rev in revisions[:num]:
        user = rev.get("user", "Unknown")
        timestamp = rev.get("timestamp", "Unknown")
        comment = rev.get("comment", "")
        print(f"- {timestamp} by {user}: {comment}")


if __name__ == "__main__":
    topic = "Python_(programming_language)"
    revisions = fetch_revisions(topic, limit=50)

    print(f"Analyzing article: {topic.replace('_', ' ')}")
    user_counts, timestamps = analyze_revisions(revisions)
    print_revision_details(revisions, num=5)

    plot_top_contributors(user_counts, top_n=10)
    plot_edits_over_time(timestamps)
