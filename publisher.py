import requests
from openai import OpenAI
from jinja2 import Template
from datetime import datetime
import os

# --- API CONFIGURATION ---
OPENAI_KEY = "your_openai_key"
NEWS_KEY = "your_newsapi_key"
PEXELS_KEY = "your_pexels_key"

client = OpenAI(api_key=OPENAI_KEY)

def fetch_news(category):
    """Gets the top headline and snippet for a category."""
    url = f"https://newsapi.org/v2/top-headlines?category={category}&language=en&apiKey={NEWS_KEY}"
    try:
        data = requests.get(url).json()
        article = data['articles'][0]
        return article['title'], article.get('description', 'Story developing...')
    except:
        return "Wires Down", "Communication with the outside world is currently limited."

def get_pexels_image(query):
    """Finds a relevant vintage-style image."""
    headers = {"Authorization": PEXELS_KEY}
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"
    try:
        res = requests.get(url, headers=headers).json()
        return res['photos'][0]['src']['large']
    except:
        return "https://via.placeholder.com/800x450?text=The+Daily+Herald"

def viola_davis_rewrite(headline, snippet, section):
    """Uses AI to channel Viola Davis and write the story."""
    prompt = f"You are Viola Davis, the world's most authoritative journalist. Write a formal, high-prestige 120-word news story for the {section} section based on this: {headline}. Context: {snippet}."
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a Pulitzer Prize-winning editor."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# --- MAIN PROCESS ---
print("Daily Herald Editorial Team is assembling...")

sections = {
    "politics": "politics",
    "sports": "sports",
    "culture": "entertainment"
}

news_data = {}

for key, cat in sections.items():
    print(f"Viola Davis is reporting on {key}...")
    h, s = fetch_news(cat)
    news_data[key] = {
        "headline": h,
        "content": viola_davis_rewrite(h, s, key),
        "image": get_pexels_image(h.split()[-1]) # Keyword search using last word
    }

# Load and Render
print("Printing today's edition...")
with open("daily_herald.html", "r") as f:
    template = Template(f.read())

final_html = template.render(
    date=datetime.now().strftime("%A, %B %d, %Y"),
    politics=news_data['politics'],
    sports=news_data['sports'],
    culture=news_data['culture']
)

# Output final file
with open("herald_published.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Done! Open 'herald_published.html' to see your newspaper.")
