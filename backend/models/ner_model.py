# Simple NER model wrapper stub
# Replace with a fine-tuned transformers pipeline when available
from typing import List, Dict

class NERModel:
    def __init__(self):
        # In a real project you might load a tokenizer and model here:
        # from transformers import pipeline
        # self.pipe = pipeline("ner", model="./my-fine-tuned-model")
        self._loaded = False

    def load(self):
        # Simulate loading
        self._loaded = True

    def extract(self, text: str) -> List[Dict]:
        """Return a list of entities in the shape {text, label, start, end}
        This is a stub for demonstration and tests.
        """
        if not self._loaded:
            self.load()

        # Naive placeholder: return any capitalized words as "PROD" entities
        entities = []
        for word in text.split():
            if word.istitle():
                start = text.find(word)
                end = start + len(word)
                entities.append({"text": word, "label": "PROD", "start": start, "end": end})
        return entities

# Provide a module-level singleton for quick use from routes
_default_model = NERModel()

def get_model():
    return _default_model
