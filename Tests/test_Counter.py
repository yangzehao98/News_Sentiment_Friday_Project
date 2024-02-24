from Classes.DataProcessor import Tokenizer, Counter, SentenceSpliter

test_sentence = 'This is a test sentence; SPY is great'
# Tokenize the news
tokenizer = Tokenizer(stop_words = 'english', lemmatize = True)
test_sentence_tokenized = tokenizer.transform(test_sentence)
news_count = Counter.run_tokens(test_sentence_tokenized)
print(news_count)
#test_list = [['test', 'sentence'], ['sentence', 'SPY'], ['SPY', 'great']]


sentence_spliter = SentenceSpliter()

# Load the article text
with open('../Tests/article.txt', 'r', encoding='utf-8') as file:
    article = file.read()

# Process the article to split into sentences
sentences = sentence_spliter.process(article)

# Print the list of sentences
for sentence in sentences:
    print(sentence)
    print("----------")