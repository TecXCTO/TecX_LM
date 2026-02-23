from transformers import pipeline

chat = pipeline("text-generation", model="./science_assistant_final")
print(chat("### User: Calculate the resonance for 8.854e-12 permittivity. ### Assistant:"))
