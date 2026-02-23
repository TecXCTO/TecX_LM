from prometheus_client import start_http_server, Gauge

# Define your 2026 Science Metrics
TRAINING_LOSS = Gauge('tecx_loss', 'Current Training Loss')
GPU_TEMP = Gauge('tecx_gpu_temp', 'GPU Temperature in Celsius')
ACCURACY = Gauge('tecx_lm_accuracy', 'Factual Accuracy Score')

# Start the metrics server on port 8000
start_http_server(8000)

# Inside your Training Loop:
# TRAINING_LOSS.set(loss.item())
# ACCURACY.set(current_val_score)













import torch
import time
import os

# --- Training Configuration ---
learning_rate = 3e-4    # How fast the model learns. Smaller is more stable for Science.
max_iters = 10000       # Total training steps
eval_interval = 500     # How often to check accuracy on "Validation Data"
eval_iters = 200        # How many batches to use for validation check
save_dir = "checkpoints"
os.makedirs(save_dir, exist_ok=True)

# 1. Initialize Model & Optimizer
# (Assumes your ResonanceLLM class is imported)
model = ResonanceLLM(vocab_size=32000).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

# 2. Setup Data Loading (Simplified for your Science JSONL)
def get_batch(split):
    # 'split' is 'train' or 'val'. This pulls a random chunk of data.
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y

# 3. The Main Loop
print("⚡ Starting Training on Science Dataset...")
start_time = time.time()

for iter in range(max_iters):

    # Periodically evaluate loss on both Train and Val sets
    if iter % eval_interval == 0 or iter == max_iters - 1:
        model.eval()
        with torch.no_grad():
            losses = torch.zeros(eval_iters)
            for k in range(eval_iters):
                X, Y = get_batch('val')
                logits, loss = model(X, Y)
                losses[k] = loss.item()
            out_loss = losses.mean()
        
        print(f"Step {iter}: Val Loss {out_loss:.4f} | Time: {time.time() - start_time:.2f}s")
        
        # Save a checkpoint of your "Resonance" Model
        torch.save(model.state_dict(), f"{save_dir}/resonance_step_{iter}.pth")
        model.train()

    # --- Core Backpropagation Step ---
    xb, yb = get_batch('train')
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True) # Set to None is faster for GPUs
    loss.backward()
    optimizer.step()

print("✅ Training Complete! Model saved in /checkpoints.")
