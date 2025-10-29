# bert/model.py


import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class SentimentAnalyzer:
    def __init__(self, model_checkpoint="cointegrated/rubert-tiny-sentiment-balanced"):
        self.model_checkpoint = model_checkpoint
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_checkpoint)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_checkpoint
        )
        if torch.cuda.is_available():
            self.model.cuda()

    def get_sentiment(self, text, return_type="score"):
        """Calculate sentiment of a text. `return_type` can be 'label', 'score' or 'proba'"""
        with torch.no_grad():
            inputs = self.tokenizer(
                text, return_tensors="pt", truncation=True, padding=True
            ).to(self.model.device)
            proba = torch.sigmoid(self.model(**inputs).logits).cpu().numpy()[0]
        if return_type == "label":
            return self.model.config.id2label[proba.argmax()]
        elif return_type == "score":
            return proba.dot([-1, 0, 1])
        return proba

    def manager_selecting(self, text):
        score = self.get_sentiment(text=text)
        with open("bert/mangers.json", "r", encoding="utf-8") as f:
            managers = json.load(f)
        for mgr in managers:
            if mgr["min_score"] <= score <= mgr["max_score"]:
                return mgr


if __name__ == "__main__":
    anal = SentimentAnalyzer()
    print(anal.manager_selecting(input(">>> ")))
