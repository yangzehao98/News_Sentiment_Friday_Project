from datetime import datetime, timedelta

import pandas as pd
from Classes.DataProcessor import NewsTokenizer, NewsSentimentAnalysis, Counter,\
    SentenceSpliter, append_dict_to_file
from Classes.Component import News

import json

from Classes.RelevanceCalculator.SimpleRelevanceCalculator import SimpleRelavanceCalculator
from Classes.SentimentModel.McdonaldModel import McdonaldModel
from Classes.SimilarityModel import TFIDFSimilarityModel

SYMBOL = 'COKE'
company_name_list = ['Coca-Cola', 'Coca Cola', 'Coke', 'KO',
                     'Coca-Cola Company', 'Coca Cola Company',
                     'Coke Company', 'COKE']

# Step 1: Read the JSON file
with open('../Data/news_data.json', 'r') as file:
    data = json.load(file)

# Step 2: Convert the list of JSON objects to a DataFrame
df = pd.DataFrame.from_dict(data)
df_recrods_test = df.to_dict('records')

# Initialize an empty list to hold the news objects
news_objects_list = []

# Iterate over each record and create a News object
for record in df_recrods_test:
    # Initialize the News object with the record (dictionary)
    news_obj = News(params=record)
    date_str = news_obj.get_params()['created_at']
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    news_obj.set_date(date)
    # Add the News object to the list
    news_objects_list.append(news_obj)

news_tokenizer = NewsTokenizer(stop_words='english', lemmatize=True)
news_sentiment_processor = NewsSentimentAnalysis()
sentence_spliter = SentenceSpliter()

for index, news in enumerate(news_objects_list):
    content = news.get_params()['content']

    # Attribute0 : Date, Time, and Company Symbol
    date_str = news.get_params()['created_at']
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    symbol = SYMBOL

    # Attribute1 : Is the news an Alert, Article, or Tweet
    author = news.get_params()['author']

    if 'Benzinga' in author:
        news_type = author.replace('Benzinga', '')
    else:
        news_type = 'article'

    # Attribute2 : Headline
    if 'Benzinga' in author:
        item_genre = 'wrap-up'
    else:
        item_genre = 'Exclusive'

    # Attribute3 : headline
    headline = news.get_params()['headline']

    # Attribute5: Prevailing Sentiment
    """portion of positive sentiment in the given sentiment counts"""
    news_tokenized = news_tokenizer.process(news)
    news_sentiment_processor.process(news, sentiment_method='mcdonald')
    total_sentiment_counts = news.get_total_sentiment_counts()
    prevailing_sentiment = McdonaldModel.calculate_positive_sentiment(total_sentiment_counts)

    # Attribute6: current sentiment
    total_count = total_sentiment_counts['neg'] + total_sentiment_counts['neu'] + total_sentiment_counts['pos']
    pos_percent = total_sentiment_counts['pos'] / total_count
    neg_percent = total_sentiment_counts['neg'] / total_count
    neu_percent = total_sentiment_counts['neu'] / total_count

    # Attribute7: Location of 1st mention
    sentence_spliter = SentenceSpliter()
    sentences = sentence_spliter.process(content)
    lofm = Counter.first_sentence_word_appearance(sentences=sentences, words=company_name_list)

    # Attribute8: Total Sentence Number
    total_sentence_number = len(sentences)

    # Attribute4 : Relevance (calculate after Attribute8)
    relevance = SimpleRelavanceCalculator.calcualte_relevance(total_sentence_number=total_sentence_number,
                                                              location_of_first_mention=lofm)

    # Attribute 9: Number of companies mentioned (how many other companies are mentioned in the news)
    other_companies_num = len(news.get_params()['symbols']) - 1

    # Attribute10: Number of words are about the company
    # TODO: go read the news and count the number of words that are about the company
    words_about_company = -1

    # Attribute11: Number of words in the news

    headline_tokens = news.get_headline_tokenized()
    content_tokens = news.get_content_tokenized()
    total_word_tokens = len(headline_tokens) + len(content_tokens)

    # Attribute12: Broker Action
    broker_action = 0

    # Attribute13: Price/Market Commentary: used to falg items describe pricing/market commentary
    # TODO: read the news and flag if it describes pricing/market commentary
    price_market_commentary = 0

    # Attribute14: Volume or News Item Count (how many news items are there rolling 2 months)
    start_date = news.get_date()
    end_date = start_date + timedelta(days=60)
    total_news_count, rolling_news_list = Counter.get_total_news_count_during_period(news_list=news_objects_list,
                                                                                     start_date=start_date,
                                                                                     end_date=end_date,
                                                                                     return_news=True)
    # Attribute15: Novelty (how many times the news is repeated in the last 2 months)
    articles = [news.get_params()['content'] for news in rolling_news_list]
    novelty = TFIDFSimilarityModel.average_pairwise_similarity(articles)

    # Attribute16: Topic Codes
    # TODO: go read the news and assign a topic code
    topic_code = 0

    # Attribute17: Other companies mentioned
    other_companies = news.get_params()['symbols'].copy()
    other_companies.remove(symbol)

    # Attribute18: Other Meta Data
    url = news.get_params()['url']
    summary = news.get_params()['summary']
    image = news.get_params()['images']
    meta_data = {'index': index, 'url': url, 'summary': summary, 'image': image}

    attribute_record = {'attribute0': {'time':date_str, 'symbol': symbol},
                        'attribute1': news_type,
                        'attribute2': item_genre,
                        'attribute3': headline,
                        'attribute4': relevance,
                        'attribute5': prevailing_sentiment,
                        'attribute6': {'positive': pos_percent, 'negative': neg_percent, 'neutral': neu_percent},
                        'attribute7': lofm,
                        'attribute8': total_sentence_number,
                        'attribute9': other_companies_num,
                        'attribute10': words_about_company,
                        'attribute11': total_word_tokens,
                        'attribute12': broker_action,
                        'attribute13': price_market_commentary,
                        'attribute14': total_news_count,
                        'attribute15': novelty,
                        'attribute16': topic_code,
                        'attribute17': other_companies,
                        'attribute18': meta_data}

    append_dict_to_file(attribute_record, 'news_attributes_test.json')
    del news





