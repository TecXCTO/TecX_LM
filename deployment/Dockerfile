# 1. Use the 2026-standard NVIDIA CUDA image
FROM nvidia/cuda:12.6.0-runtime-ubuntu22.04

# 2. Install Python and system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy your project files into the container
COPY . /app

# 5. Install Python libraries
RUN pip3 install --no-cache-dir -r requirements.txt

# 6. Expose the Gradio port (7860 is the default)
EXPOSE 7860

# 7. Command to start your Science LLM Web UI
CMD ["python3", "tecx_Chat_Web-UI.py"]
