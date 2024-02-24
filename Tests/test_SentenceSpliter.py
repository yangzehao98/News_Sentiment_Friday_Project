from Classes.DataProcessor import SentenceSpliter

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

#print(sentences)


