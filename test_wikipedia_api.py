import requests

def get_wikipedia_summary(title):
    # Wikipedia REST API endpoint for page summaries
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No summary available.")
    else:
        return "Error: Could not retrieve page."

if __name__ == "__main__":
    topic = "Python_(programming_language)"  # example topic
    summary = get_wikipedia_summary(topic)
    print(f"Summary of {topic}:\n{summary}")
