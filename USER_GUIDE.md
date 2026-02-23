# Quick Start

Install Docker: Ensure you have the NVIDIA Container Toolkit installed to access your GPUs.
Pull & Run:
```
bash
docker pull your-username/resonance-ai:latest
docker run --gpus all -p 7860:7860 resonance-ai
```
Access the UI: Open http://localhost:7860 in your browser to start chatting with the Science Assistant.

# Example Prompts

"Explain the relationship between vacuum permittivity and resonant frequency."
"Calculate the capacitance needed for a 2.45 GHz resonance if 
 is constant."
"Write a Python script to simulate a 3D harmonic oscillator."
