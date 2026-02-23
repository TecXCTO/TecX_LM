import json
import re
import hashlib
from crawl4ai import WebCrawler # Optimized for LLM data extraction

# 1. Basic Cleaning Function
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace/newlines
    text = re.sub(r'[^\x00-\x7F]+', ' ', text) # Remove non-ASCII characters
    return text.strip()

# 2. Simple Deduplication (using MD5 Hashing)
seen_hashes = set()

def is_duplicate(text):
    text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    if text_hash in seen_hashes:
        return True
    seen_hashes.add(text_hash)
    return False

# 3. Main Automation Loop
def build_llm_dataset(urls, output_file):
    crawler = WebCrawler()
    crawler.warmup()

    with open(output_file, 'a', encoding='utf-8') as f:
        for url in urls:
            # Crawl4AI extracts clean Markdown/Text automatically
            result = crawler.run(url=url)
            raw_content = result.markdown if result.markdown else result.extracted_content
            
            cleaned = clean_text(raw_content)

            # Quality Check: Minimum length & Deduplication
            if len(cleaned) > 500 and not is_duplicate(cleaned):
                data_entry = {
                    "text": cleaned,
                    "source": url,
                    "token_estimate": len(cleaned) // 4 # Rough estimate
                }
                f.write(json.dumps(data_entry) + '\n')
                print(f"✅ Added: {url}")
            else:
                print(f"❌ Skipped (Too short or duplicate): {url}")

# --- Execution ---
science_urls = [
    "https://en.wikipedia.org",
    "https://en.wikipedia.org",
    # Add thousands of URLs here
]

build_llm_dataset(science_urls, "science_pretrain_data.jsonl")
