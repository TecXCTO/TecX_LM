from transformers import BitsAndBytesConfig

# 2026 Best-Practice Quantization Config
quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",      # Optimized for scientific data distribution
    bnb_4bit_compute_dtype=torch.bfloat16, # Keeps math fast on Blackwell/Ada
    bnb_4bit_use_double_quant=True  # Compresses the quantization constants too!
)

model = AutoModelForCausalLM.from_pretrained(
    "./science_assistant_final",
    quantization_config=quant_config,
    device_map="auto"
)
