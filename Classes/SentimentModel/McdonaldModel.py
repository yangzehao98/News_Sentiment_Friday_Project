from typing import List
from Classes.SentimentModel.SingletonSentimentModel import SingletonSentimentModel
import pandas as pd

# Path: C:\Users\wzy\Documents\News_Sentiment_Friday_Project\Data
class McdonaldModel(metaclass=SingletonSentimentModel):
    def __init__(self):
        self.model = "mcdonald"
        self.word_sentiment = pd.read_csv('../Data/word_sentiment.csv')
        self.sentiment_dict = self.word_sentiment.set_index('Word')['Sentiment'].to_dict()

    def process(self, sentence_tokenized: List[str]):
        # TODO: Implement the McDonald Model; and return the sentiment dict
        sentiment_counts = {'neg': 0, 'neu': 0, 'pos': 0}

        # Process each tokenized word
        for word in sentence_tokenized:
            # Retrieve the sentiment score for the word, default to neutral (0) if not found
            word_sentiment = self.sentiment_dict.get(word.lower(), 0)
            # Increment the sentiment counts based on the word's sentiment
            if word_sentiment > 0:
                sentiment_counts['pos'] += 1
            elif word_sentiment < 0:
                sentiment_counts['neg'] += 1
            else:
                sentiment_counts['neu'] += 1

        # Here you might want to normalize or convert counts to probabilities
        # For simplicity, let's assume we just return the raw counts
        return sentiment_counts
        #pass


