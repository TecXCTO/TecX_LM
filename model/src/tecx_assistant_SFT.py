from trl import SFTTrainer
from transformers import TrainingArguments, AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig
import torch

# 1. Load your Pre-trained Model and Custom Tokenizer
model_path = "../checkpoints/tecx_final_model" 
tokenizer = AutoTokenizer.from_file("../science_tokenizer.json")
tokenizer.pad_token = tokenizer.eos_token # Essential for batching

# 2. Configure LoRA (Saves 70% VRAM)
# This targets the "Resonance" layers specifically
peft_config = LoraConfig(
    r=16, 
    lora_alpha=32, 
    target_modules=["q_proj", "v_proj"], # Targets Attention heads
    lora_dropout=0.05, 
    bias="none", 
    task_type="CAUSAL_LM"
)

# 3. Setup Training Arguments for 2026
training_args = TrainingArguments(
    output_dir="../tecx_assistant_v1",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4, # Simulates a larger batch size
    learning_rate=2e-4,
    logging_steps=10,
    num_train_epochs=3, # 3 passes over your instruction data is usually enough
    bf16=True,           # Optimized for H100/RTX 6000 Ada
    save_strategy="epoch",
    report_to="none"
)

# 4. Initialize the SFT Trainer
trainer = SFTTrainer(
    model=model_path,
    train_dataset="../science_instructions.jsonl", # Your User/Assistant pairs
    dataset_text_field="text", # The field in your JSONL
    max_seq_length=2048,
    tokenizer=tokenizer,
    args=training_args,
    peft_config=peft_config,
)

# 5. Execute Fine-Tuning
print("🤖 Converting Science Model to Assistant...")
trainer.train()

# 6. Save the final Chat Model
trainer.save_model("../tecx_assistant_final")
print("✅ Your Science Assistant is ready!")
