import numpy as np
import pandas as pd
from Classes.DataProcessor import Tokenizer, NewsTokenizer, NewsSentimentAnalysis, SentenceSentimentAnalysis, Counter
from Classes.Component import News
import json
import pandas as pd

# Step 1: Read the JSON file
with open('news_data.json', 'r') as file:
    data = json.load(file)

# Step 2: Convert the list of JSON objects to a DataFrame
df = pd.DataFrame.from_dict(data)
df_recrods_test = df.to_dict('records')[0:5]


# Initialize an empty list to hold the news objects
news_objects_list = []

# Iterate over each record and create a News object
for record in df_recrods_test:
    # Initialize the News object with the record (dictionary)
    news_obj = News(params=record)
    # Add the News object to the list
    news_objects_list.append(news_obj)

news_tokenizer = NewsTokenizer(stop_words='english', lemmatize=True)
news_sentiment_processor = NewsSentimentAnalysis()

for news in news_objects_list:
    news_tokenized = news_tokenizer.process(news)






