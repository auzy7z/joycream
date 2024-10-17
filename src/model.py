from transformers import pipeline
import json

# Load config
with open('../config/config.json') as f:
    config = json.load(f)

# Load model
generator = pipeline("text-generation", model=config['gpt_model'])

def generate_response(message):
    result = generator(message, max_length=config['max_length'], num_return_sequences=1)
    return result[0]['generated_text']
