import json
import ollama  # Ensure Ollama is installed and running locally

INPUT_FILE = "science_pretrain_data.jsonl"
OUTPUT_FILE = "gold_standard_science_data.jsonl"

def judge_quality(text):
    """Asks a local LLM if the text is high-quality for training."""
    prompt = f"""
    You are an expert data quality judge for scientific LLM training.
    Evaluate the following text for:
    1. Scientific accuracy.
    2. Lack of 'noise' (ads, navigation menus, broken characters).
    3. Clear educational value.

    Text: {text[:1000]}... (truncated)

    Does this text meet high-quality standards for pre-training? 
    Answer ONLY with 'YES' or 'NO'.
    """
    
    try:
        response = ollama.generate(model='llama3', prompt=prompt)
        decision = response['response'].strip().upper()
        return "YES" in decision
    except Exception as e:
        print(f"Error judging text: {e}")
        return False

# --- Main Automation Loop ---
print("🚀 Starting AI-powered data filtration...")

with open(INPUT_FILE, 'r', encoding='utf-8') as infile, \
     open(OUTPUT_FILE, 'a', encoding='utf-8') as outfile:
    
    for line in infile:
        entry = json.loads(line)
        raw_text = entry.get("text", "")

        # Ask the AI Judge
        if judge_quality(raw_text):
            print(f"✅ PASSED: {entry.get('source')}")
            outfile.write(json.dumps(entry) + '\n')
        else:
            print(f"❌ REJECTED: {entry.get('source')}")

print(f"✨ Automation complete! High-quality data saved to {OUTPUT_FILE}")
