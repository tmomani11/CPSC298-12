# Wikipedia as Social Media: Collaboration and Governance

## Group Members
- Tyler Momani  
- Dylan Massaro  
- Alejandro O’Beirne Serrano  

**Literature Review:** [literature.md](literature.md)

---

## Abstract
This project looks at how Wikipedia can be seen as a kind of social media, not just an encyclopedia. Unlike places like Reddit or Twitter, it doesn’t have likes, karma, or follower counts, but it still manages to attract huge participation and collective knowledge built over time. The way people use talk pages, get into edit wars, or show bursts of activity makes it feel similar to other social platforms, even though its design is much more stripped down. We want to understand how this setup shapes community rules, editor motivation, and the quality of what gets produced. In the end, the project asks whether Wikipedia’s model can teach other platforms how to create healthier engagement and more trust without relying on the usual social media features.

---

## Research Questions
1. **How does the absence of likes, follower counts, and other common social media features shape participation and motivation on Wikipedia?**  
   We want to test whether participation thrives differently when gamification is removed.  

2. **In what ways do talk pages, edit wars, and bursts of editing reflect both the fallibilities of human psychology and the community’s ability to manage them?**  
   Here we focus on conflict dynamics and collaboration.  

3. **Which aspects of Wikipedia’s institutional design (such as open edit histories, transparent governance, and cultural norms) encourage more rational collaboration despite conflict and bias?**  
   We want to see if these practices can explain sustained engagement without upvotes.  

4. **Could these design features be adapted by other platforms to promote healthier engagement and improve trust in shared information?**  
   This addresses the broader social media design implications.  

---

## Methodology
- **Data Collection**: Use the Wikipedia API to gather revision histories, talk page edits, and pageview statistics.  
- **Comparative Analysis**: Compare Wikipedia’s participation dynamics to platforms like Reddit or Twitter, which include visible karma/likes.  
- **Future Work**: Expand analysis to measure participation burstiness, conflict resolution, and governance in action.  

---
## 🧩 Prototype Program
The file `week7.py` demonstrates how to connect to the Wikipedia API and fetch information.  
Currently, it retrieves article summaries and recent revisions, and also compares average daily pageviews for multiple topics.

---

## 🧠 Research Question – Week 7
**Which of several Wikipedia topics gets the most sustained attention (average daily pageviews) over the last 30 days?**

---

## 📊 Methodology
- For each page, call the **Wikimedia Pageviews REST API** to fetch daily pageviews for the last 30 complete days.  
- Compute **total** and **average per day** for each page.  
- Rank topics by **average daily pageviews** (a more stable measure than single-day spikes).  
- Save results to a **CSV file** (`results_week7.csv`) for reproducibility.

---

## ⚙️ How to Run
1. Make sure Python 3 is installed.  
2. Install the required dependency:
   ```bash
   pip install requests
3. Python3 hw7.py

## How These Results Answer the Question
By averaging daily pageviews over a 30-day window, the program identifies which topic sustains the most continuous attention rather than short bursts of popularity.
The topic with the highest average daily views (Artificial intelligence) therefore represents the one that garners the most persistent, ongoing public interest among the compared topics.
