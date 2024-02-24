# Tokenize the news
from Classes.DataProcessor import Tokenizer

test_sentence = 'This is a test sentence; SPY is great'
tokenizer = Tokenizer(stop_words = 'english', lemmatize = True)
test_sentence_tokenized = tokenizer.transform(test_sentence)
print(test_sentence_tokenized)

test_sentence2 = "Just to be prudent, we took about 20% off the table,” Mahoney said."
test_sentence_tokenized2 = tokenizer.transform(test_sentence2)
print(test_sentence_tokenized2)