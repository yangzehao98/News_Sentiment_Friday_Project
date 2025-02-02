from typing import Optional, List
from Classes.Component import News
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from Classes.SentimentModel.McdonaldModel import McdonaldModel
from collections import Counter as CollectionsCounter
import json
# Ensure required resources are downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class Tokenizer:

    def __init__(self, stop_words: str = 'english', lemmatize: bool = True):
        self.stop_words = stop_words
        self.lemmatize = lemmatize
        self._tokenizer = None # sklearn tokenizer if possible
        if stop_words == 'english':
            self.stop_words = set(stopwords.words('english'))
        else:
            self.stop_words = set()

        self.lemmatizer = WordNetLemmatizer() if lemmatize else None

    def transform(self, sentence: str) -> list[str]:
        """
        This function should tokenize the sentence and return a list of tokens.
        Process the sentence by removing stop words and lemmatizing the words if lemmatize is set to True.
        :param sentence: str
        :return: list[str]
        e.g. "This is a test sentence; SPY is great" -> ['test', 'sentence', 'SPY', 'great']
        """
        # Tokenize the sentence
        tokens = word_tokenize(sentence)

        # Remove stop words and punctuation
        tokens = [token for token in tokens if token.isalpha() and token.lower() not in self.stop_words]

        # Lemmatize the words if lemmatization is enabled
        if self.lemmatize:
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return tokens


class NewsTokenizer:
    def __init__(self, stop_words: str = 'english', lemmatize: bool = True):
        self.stop_words = stop_words
        self.lemmatize = lemmatize
        self.tokenizer = Tokenizer(stop_words, lemmatize)

    def process(self, news: News):
        """
        This function should tokenize the headline and content of the news.
        :param news: News class
        """
        news_headline = news.get_params()['headline']
        news_content = news.get_params()['content']
        news_headline_tokenized = self.tokenizer.transform(news_headline)
        news_content_tokenized = self.tokenizer.transform(news_content)
        news.set_tokenized(True)
        news.set_params({'headline_tokenized': news_headline_tokenized, 'content_tokenized': news_content_tokenized})



class NewsSentimentAnalysis:
    def process(self, news: News, sentiment_method: str):
        """
        This function should analyze the sentiment of the news.
        Take the headline setense and content sentence and analyze the sentiment of each sentence.
        :param news: News class
        :param sentiment_model: sentiment model to use - just use McDonald for now
        """

        headline_tokenized = news.get_params()['headline_tokenized']
        content_tokenized = news.get_params()['content_tokenized']
        sen_model = SentenceSentimentAnalysis()
        news_headline_sentiment = sen_model.process(sentence_tokenized = headline_tokenized, sentiment_method = sentiment_method)
        news_content_sentiment = sen_model.process(sentence_tokenized = content_tokenized, sentiment_method = sentiment_method)
        news.set_sentiment_analyzed(True)
        news.set_sentiment({'headline_sentiment': news_headline_sentiment, 'content_sentiment': news_content_sentiment})
        total_sentiment = {'neg': news_headline_sentiment['neg'] + news_content_sentiment['neg'],
                             'neu': news_headline_sentiment['neu'] + news_content_sentiment['neu'],
                            'pos': news_headline_sentiment['pos'] + news_content_sentiment['pos']}
        news.set_sentiment({'total_sentiment_counts': total_sentiment})


class SentenceSentimentAnalysis:

    def __init__(self):
        self.sentiment_model = None
    def process(self, sentence: Optional[str] = None, sentence_tokenized: Optional[List[str]] = None,
                sentiment_method: str = 'mcdonald'):
        """
        This function should analyze the sentiment of the sentence. That is, counting
        the number of positive, negative and neutral words in the sentence within the McDonald's dictionary.

        Or you can alwasy, just adding the probability of being positive, negative and neutral based on the McDonald's dictionary.
        And aggregate the probabilities of each word in the sentence in a way.
        :param sentence: This should just be a sentence, e.g. "This is a test sentence; SPY is great"
        :param sentence_tokenized: This should be a tokenized sentence, e.g. ['test', 'sentence', 'SPY', 'great']
        :param sentiment_model: sentiment model to use - just use McDonald for now
        :return: dict: {'neg': 0.0, 'neu': 0.238, 'pos': 0.762}
        """

        if self.sentiment_model is None:
            if sentiment_method == 'mcdonald':
                self.sentiment_model = McdonaldModel()
            else:
                raise ValueError('Sentiment method not supported')
        if sentiment_method!=self.sentiment_model.model:
            if sentiment_method == 'mcdonald':
                self.sentiment_model = McdonaldModel()
            else:
                raise ValueError('Sentiment method not supported')
        sentiment = self.sentiment_model.process_tokenized_sentence(sentence_tokenized)
        return sentiment

class Counter:
    @classmethod
    def run_tokens(cls, tokens: list[str]) -> dict:
        """
        Count the token frequency and return the result as a dictionary.
        :param tokens: list[str]: e.g. ['test', 'sentence', 'sentence', 'SPY', 'great']
        :return: dict , e.g. {'test': 1, 'sentence': 2, 'SPY': 1, 'great': 1}
        """
        return dict(CollectionsCounter(tokens))


    @classmethod
    def run_list_of_tokens(cls, list_of_token: list[str]) -> [dict]:
        """
        Count the token frequency and return the result as a dictionary.
        :param list_of_token: list[list[str]]: e.g. [['test', 'sentence'], ['sentence', 'SPY'], ['SPY', 'great']]
        :return: List[dict] , e.g. [{'test': 1, 'sentence': 1}, {'sentence': 1, 'SPY': 1}, {'SPY': 1, 'great': 1}]
        """
        return [dict(CollectionsCounter(tokens)) for tokens in list_of_token]

    @classmethod
    def first_sentence_word_appearance(cls, sentences: list[str], words: List[str]) -> Optional[int]:
        for index, sentence in enumerate(sentences):
            if any(word in sentence for word in words):
                return index
        return None

    @classmethod
    def get_total_news_count_during_period(cls, news_list: List[News], start_date: str,
                                           end_date: str, return_news: bool = False) -> [int, Optional[List[News]]]:
        count = 0
        news_to_return = []
        for news in news_list:
            if start_date <= news.get_date() <= end_date:
                news_to_return.append(news)
                count += 1
        if return_news:
            return count, news_to_return
        return count



class SentenceSpliter:
    def process(self, text: str) -> List[str]:
        """
        This function should split the text into sentences.
        :param text: str
        :return: List[str]

        """
        sentences = sent_tokenize(text)
        return sentences

def append_dict_to_file(dict_data: dict, file_path: str):
    with open(file_path, 'a') as file:  # Open file in append mode
        json.dump(dict_data, file)  # Dump dictionary to file
        file.write('\n')  # Write a newline character after the dictionary for readability
