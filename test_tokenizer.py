from tokenizers import Tokenizer

# Load your custom science tokenizer
sci_tokenizer = Tokenizer.from_file("science_tokenizer.json")

text = "The vacuum permittivity is 8.854e-12 F/m."
output = sci_tokenizer.encode(text)

print(f"Tokens: {output.tokens}")
print(f"Token IDs: {output.ids}")
