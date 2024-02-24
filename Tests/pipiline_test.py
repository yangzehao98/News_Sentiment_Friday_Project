import pandas as pd
import numpy as np
from Classes.DataPreprocessing import Tokenizer, NewsTokenizer, NewsSentimentAnalysis, SentenceSentimentAnalysis, Counter
from Classes.Element import News

test_news_data = {'headline': 'This is a test headline', 'content': 'This is a test content; it is a very good content'}
test_news = News(params = test_news_data)
test_sentence = 'This is a test sentence; SPY is great'

# Tokenize the news
tokenizer = Tokenizer(stop_words = 'english', lemmatize = True)
test_sentence_tokenized = tokenizer.transform(test_sentence)
# test_sentence should be like = ['test', 'sentence', 'SPY', 'great']


news_tokenizer = NewsTokenizer(stop_words = 'english', lemmatize = True)
tokenizer.process(test_news)
test_news_params = test_news.get_params()
# test_news_params should be like = {'headline': ['test', 'headline'], 'content': ['test', 'content', 'good', 'content']}

# Sentiment Analysis
sentiment_processor = SentenceSentimentAnalysis()
# test_sentence_sentiment_vader = sentiment_processor.process(sentence = test_sentence, sentiment_model = 'vader')
test_sentence_sentiment_mcdonald = sentiment_processor.process(sentence = test_sentence, sentiment_model = 'mcdonald')
# test_sentence_sentiment_xxx should be like = {'neg': 0.0, 'neu': 0.238, 'pos': 0.762}

news_sentiment_processor = NewsSentimentAnalysis()
# test_news_sentiment_vader = news_sentiment_processor.process(news = test_news, sentiment_model = 'vader')
test_news_sentiment_mcdonald = news_sentiment_processor.process(news = test_news, sentiment_model = 'mcdonald')

test_news_sentiment = news_sentiment_processor.process(test_news)

test_news_sentiemnt = test_news.get_sentiment()
# test_news_sentiment should be like = {'headline': {'neg': 0.0, 'neu': 0.238, 'pos': 0.762}, 'content': {'neg': 0.0, 'neu': 0.238, 'pos': 0.762}}

# Counter for the news
news_count = Counter.run(test_sentence_tokenized)
test_news.run_counter() # This should be able to run after tokenization
test_news_word_counter = test_news.get_count_results()
