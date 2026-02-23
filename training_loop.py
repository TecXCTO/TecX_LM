from prometheus_client import start_http_server, Gauge

# Define your 2026 Science Metrics
TRAINING_LOSS = Gauge('resonance_loss', 'Current Training Loss')
GPU_TEMP = Gauge('resonance_gpu_temp', 'GPU Temperature in Celsius')
ACCURACY = Gauge('resonance_science_accuracy', 'Factual Accuracy Score')

# Start the metrics server on port 8000
start_http_server(8000)

# Inside your Training Loop:
# TRAINING_LOSS.set(loss.item())
# ACCURACY.set(current_val_score)
