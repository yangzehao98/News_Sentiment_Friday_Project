from Classes.DataProcessor import Tokenizer, NewsTokenizer, NewsSentimentAnalysis, SentenceSentimentAnalysis, Counter
from Classes.Component import News
test_sentence = 'This is a test sentence; SPY is great'

# Tokenize the news
tokenizer = Tokenizer(stop_words = 'english', lemmatize = True)
test_sentence_tokenized = tokenizer.transform(test_sentence)
# test_sentence should be like = ['test', 'sentence', 'SPY', 'great']
sentiment_processor = SentenceSentimentAnalysis()
# test_sentence_sentiment_vader = sentiment_processor.process(sentence = test_sentence, sentiment_model = 'vader')
test_sentence_sentiment_mcdonald = sentiment_processor.process(sentence_tokenized = test_sentence_tokenized, sentiment_method = 'mcdonald')
# test_sentence_sentiment_xxx should be like = {'neg': 0.0, 'neu': 0.238, 'pos': 0.762}
print(test_sentence_sentiment_mcdonald)