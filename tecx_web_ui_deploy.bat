# Build the Image:
docker build -t resonance-science-ai .
# Run on your GPU:
docker run --gpus all -p 7860:7860 resonance-science-ai
