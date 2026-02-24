from transformers import AutoProcessor, LlavaForConditionalGeneration
import torch
from PIL import Image

# 1. Load the Multi-Modal Resonance Engine
model_id = "tecx-ai/vision-v2"
processor = AutoProcessor.from_pretrained(model_id)
model = LlavaForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

# 2. Analyze a Circuit Diagram
def analyze_diagram(image_path):
    raw_image = Image.open(image_path)
    prompt = "USER: <image>\nIdentify the resonance components in this diagram. ASSISTANT:"
    
    inputs = processor(prompt, raw_image, return_tensors='pt').to(0, torch.bfloat16)
    output = model.generate(**inputs, max_new_tokens=200)
    
    print(processor.decode(output[0], skip_special_tokens=True))

# analyze_diagram("oscillator_schematic.png")
