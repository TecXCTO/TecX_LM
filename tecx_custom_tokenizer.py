from tokenizers import Tokenizer, models, trainers, pre_tokenizers, decoders, processors
import os

# 1. Initialize a BPE (Byte-Pair Encoding) Model
# BPE is the best choice for scientific text as it handles rare words well.
tokenizer = Tokenizer(models.BPE(unk_token="[UNK]"))

# 2. Setup Pre-tokenization (How to split the initial text)
# We use a ByteLevel pre-tokenizer to handle whitespace and special symbols correctly.
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)

# 3. Define the Trainer
# VOCAB_SIZE: 32,000 to 50,000 is standard for a specialized model.
# MIN_FREQUENCY: Only words appearing 2+ times become tokens.
trainer = trainers.BpeTrainer(
    vocab_size=32000, 
    min_frequency=2, 
    special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
)

# 4. Point to your "Gold Standard" Science JSONL file
data_files = ["gold_standard_science_data.jsonl"]

def batch_iterator(batch_size=1000):
    for i in range(0, len(data_files)):
        with open(data_files[i], "r", encoding="utf-8") as f:
            for line in f:
                yield json.loads(line)

# 5. Start the Training Process
print("🧬 Training Science Tokenizer... This may take a few minutes.")
tokenizer.train_from_iterator(batch_iterator(), trainer=trainer)

# 6. Save the Tokenizer
tokenizer.save("science_tokenizer.json")
print("✅ Tokenizer saved as 'science_tokenizer.json'!")
