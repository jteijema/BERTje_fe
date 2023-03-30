from asreview.models.feature_extraction.base import BaseFeatureExtraction
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

class BERTje(BaseFeatureExtraction):
    name = "bertje"
    label = "BERTje"

    def __init__(self):
        super(BERTje, self).__init__()
        self.tokenizer = AutoTokenizer.from_pretrained("GroNLP/bert-base-dutch-cased")
        self.model = AutoModel.from_pretrained("GroNLP/bert-base-dutch-cased")

    def transform(self, texts):
        if isinstance(texts, str):
            texts = [texts]

        # Create default embeddings for empty strings
        default_embedding = np.zeros((1, self.model.config.hidden_size))

        embeddings = []
        for text in texts:
            if text.strip() == "":
                embeddings.append(default_embedding)
            else:
                inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True)
                with torch.no_grad():
                    outputs = self.model(**inputs)
                embedding = outputs.last_hidden_state.mean(dim=1).numpy()
                embeddings.append(embedding)

        return np.concatenate(embeddings, axis=0)
