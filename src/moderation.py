from transformers import pipeline

# Load toxicity detector
toxicity_detector = pipeline("text-classification", model="unitary/toxic-bert")

def is_toxic(message):
    result = toxicity_detector(message)
    return result[0]['label'] == 'TOXIC'
