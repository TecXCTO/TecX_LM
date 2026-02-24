import os
import requests
from datetime import datetime, timedelta
import ollama # Or The TecX-LLM endpoint

# --- Configuration ---
GITHUB_REPO = "TecXCTO/TecX_LM"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
NEWSLETTER_FILE = f"newsletter_{datetime.now().strftime('%Y_%m')}.md"

def get_monthly_updates():
    """Fetches commits and issues from the last 30 days."""
    since = (datetime.now() - timedelta(days=30)).isoformat()
    url = f"https://api.github.com{GITHUB_REPO}/issues?since={since}&state=all"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    return response.json()

def generate_newsletter(data):
    """Uses TecX-LLM to summarize the scientific progress."""
    summary_text = "\n".join([f"- {item['title']}: {item['body'][:200]}" for item in data])
    
    prompt = f"""
    You are the lead editor for the 'TecX-AI' Monthly Newsletter.
    Based on the following GitHub updates, write a professional report for physicists and AI engineers.
    
    Focus on:
    1. New physics logic added (e.g., updates to epsilon zero calculations).
    2. Hardware performance gains on B300/H300 clusters.
    3. Community highlights (Top contributors).

    Updates:
    {summary_text}
    """
    
    # Using the TecX model to write its own update!
    response = ollama.generate(model='tecx-llm', prompt=prompt)
    return response['response']

# --- Execution ---
updates = get_monthly_updates()
newsletter_content = generate_newsletter(updates)

with open(NEWSLETTER_FILE, "w") as f:
    f.write(f"# 🔬 TecX-AI: Monthly Progress Report (Feb 2026)\n\n")
    f.write(newsletter_content)

print(f"✅ Newsletter generated: {NEWSLETTER_FILE}")
