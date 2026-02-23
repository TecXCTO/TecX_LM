import json
import ollama
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Settings ---
INPUT_FILE = "science_pretrain_data.jsonl"
OUTPUT_FILE = "gold_standard_science_data.jsonl"
NUM_WORKERS = 10  # Number of parallel "Judges". Increase based on your GPU VRAM.

def judge_quality(line):
    """Processes a single line from the JSONL and returns it if high quality."""
    entry = json.loads(line)
    text = entry.get("text", "")[:1500] # Analyze the first 1500 chars for speed

    prompt = f"Analyze if this scientific text is high-quality for LLM training. Answer 'YES' or 'NO' only: {text}"
    
    try:
        # Use a fast model like 'mistral' or 'llama3:8b-instruct-q4_K_M'
        response = ollama.generate(model='llama3', prompt=prompt)
        if "YES" in response['response'].upper():
            return entry
    except Exception:
        return None
    return None

# --- Automated Parallel Processing ---
print(f"🚀 Starting High-Speed Filtration with {NUM_WORKERS} workers...")

with open(INPUT_FILE, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

results_count = 0
with open(OUTPUT_FILE, 'a', encoding='utf-8') as outfile:
    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        # Submit all lines to the thread pool
        future_to_line = {executor.submit(judge_quality, line): line for line in lines}
        
        for future in as_completed(future_to_line):
            result = future.result()
            if result:
                outfile.write(json.dumps(result) + '\n')
                results_count += 1
                if results_count % 10 == 0:
                    print(f"✅ {results_count} high-quality samples saved...")

print(f"✨ Done! Processed {len(lines)} items. Saved {results_count} to {OUTPUT_FILE}.")
