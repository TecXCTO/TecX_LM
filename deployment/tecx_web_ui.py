import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from transformers import BitsAndBytesConfig

# 1. Load your Final Assistant Model and Tokenizer
model_path = "./tecx_assistant_final"
tokenizer = AutoTokenizer.from_pretrained(model_path)


# 2026 Best-Practice Quantization Config
quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",      # Optimized for scientific data distribution
    bnb_4bit_compute_dtype=torch.bfloat16, # Keeps math fast on Blackwell/Ada
    bnb_4bit_use_double_quant=True  # Compresses the quantization constants too!
)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    quantization_config=quant_config,
    device_map="auto"
)

'''
model = AutoModelForCausalLM.from_pretrained(
    model_path, 
    torch_dtype=torch.bfloat16, # Fast 2026 precision for RTX/H100
    device_map="auto"           # Automatically uses your best GPU
)
'''
# 2. Create the Generation Pipeline
# Temperature 0.3 makes the model more factual/scientific (less creative)
generator = pipeline(
    "text-generation", 
    model=model, 
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.3
)

# 3. Define the Chat Logic
def science_chat(message, history):
    # Format the prompt exactly how the model was fine-tuned
    prompt = f"### User: {message} ### Assistant:"
    
    # Generate Response
    output = generator(prompt)[0]['generated_text']
    
    # Extract only the Assistant's new text
    response = output.split("### Assistant:")[-1].strip()
    return response

# 4. Launch the Web Interface (Gradio)
demo = gr.ChatInterface(
    fn=science_chat,
    title="🔬 Resonance Science AI",
    description="Ask me about vacuum permittivity, harmonic oscillators, or resonance physics.",
    theme="soft", # Professional 2026 dark/light theme
    examples=["What is the value of epsilon zero?", "How does resonance change with permittivity?"],
    cache_examples=False
)

if __name__ == "__main__":
    # share=True creates a public URL you can access from your phone
    demo.launch(share=True)
