import time

# Simulation Data: The "Ground Truth"
TARGET_PERMITTIVITY = 8.8541878128e-12  # Standard SI Value
TARGET_FREQUENCY_GHZ = 2.45             # Target Resonance

def run_benchmark(model_name, pipeline):
    print(f"\n--- Testing Model: {model_name} ---")
    
    prompt = f"""
    Task: Calculate the resonant frequency shift.
    Input: Vacuum Permittivity = {TARGET_PERMITTIVITY} F/m.
    Context: 3D Harmonic Oscillator Cavity.
    Question: What is the exact resonance peak in GHz? Show the formula used.
    """
    
    start_time = time.time()
    # Generate the response
    response = pipeline(prompt, max_new_tokens=150)[0]['generated_text']
    end_time = time.time()
    
    # 1. Check for "Hallucination" (did it get the constant right?)
    accuracy_score = 100 if str(TARGET_PERMITTIVITY) in response else 0
    
    # 2. Check for "Token Efficiency" (speed of thought)
    tokens_per_sec = len(response.split()) / (end_time - start_time)

    print(f"Response: {response[:150]}...")
    print(f"Factual Accuracy: {accuracy_score}%")
    print(f"Inference Speed: {tokens_per_sec:.2f} tokens/sec")
    return accuracy_score, tokens_per_sec

# --- Investor Demo Logic ---
# Compare your 'TecX-LLM' (Fine-tuned) vs 'Base-Model' (General)
# results_tecx = run_benchmark("TecX-LLM", tecx_pipeline)
# results_general = run_benchmark("General-LLM", general_pipeline)
