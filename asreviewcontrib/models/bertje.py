from asreview.models.feature_extraction.base import BaseFeatureExtraction
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from tqdm import tqdm

class BERTje(BaseFeatureExtraction):
    name = "bertje"
    label = "bertje"

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
        for text in tqdm(texts, desc="Processing texts"):
            if text.strip() == "":
                embeddings.append(default_embedding)
            else:
                inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True)
                with torch.no_grad():
                    outputs = self.model(**inputs)
                embedding = outputs.last_hidden_state.mean(dim=1).numpy()
                embeddings.append(embedding)

        return np.concatenate(embeddings, axis=0)
