# Build the Image:
docker build -t tecx-science-ai .
# Run on your GPU:
docker run --gpus all -p 7860:7860 tecx-science-ai
