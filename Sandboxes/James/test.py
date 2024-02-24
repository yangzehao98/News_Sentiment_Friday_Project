import pandas as pd
import numpy as np
from Classes.DataProcessor import Tokenizer, NewsTokenizer, NewsSentimentAnalysis, SentenceSentimentAnalysis, Counter
from Classes.Component import News

test_news_data = {'symbol': 'COKE', 'headline': 'This is a test headline', 'content': 'This is a test content; it is a very good content'}
test_news = News(params = test_news_data)
test_sentence = 'This is a test sentence; SPY is great'

# Tokenize the news
tokenizer = Tokenizer(stop_words = 'english', lemmatize = True)
test_sentence_tokenized = tokenizer.transform(test_sentence)
print(test_sentence_tokenized)
# test_sentence should be like = ['test', 'sentence', 'SPY', 'great']
