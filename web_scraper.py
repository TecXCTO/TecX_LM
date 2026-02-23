import requests
from bs4 import BeautifulSoup
import json

def scrape_to_dataset(url, output_file):
    try:
        # Fetch the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all paragraph text
        paragraphs = [p.get_text().strip() for p in soup.find_all('p') if len(p.get_text()) > 20]
        full_text = " ".join(paragraphs)

        # Prepare the JSONL entry
        data_entry = {
            "text": full_text,
            "metadata": {
                "source": url,
                "length": len(full_text)
            }
        }

        # Append to the JSONL file
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data_entry) + '\n')
            
        print(f"Successfully scraped: {url}")

    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Example Usage
scrape_to_dataset("https://example.com/science-article", "my_dataset.jsonl")
