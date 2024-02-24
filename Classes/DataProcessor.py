from typing import Optional, List

from Classes.Component import News


class Tokenizer:

    def __init__(self, stop_words: str = 'english', lemmatize: bool = True):
        self.stop_words = stop_words
        self.lemmatize = lemmatize
        self._tokenizer = None # sklearn tokenizer if possible
        pass

    def transform(self, sentence: str) -> list[str]:
        """
        This function should tokenize the sentence and return a list of tokens.
        Process the sentence by removing stop words and lemmatizing the words if lemmatize is set to True.
        :param sentence: str
        :return: list[str]
        e.g. "This is a test sentence; SPY is great" -> ['test', 'sentence', 'SPY', 'great']
        """
        pass

    def process(self, sentence: str):
        """
        Each sentence should be lemmaized and stop words removed. Then the sentence should be tokenized.
        :param sentence: str
        :return: list[str]
        """
        pass


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
        news_headline_tokenized = self.tokenizer.process(news_headline)
        news_content_tokenized = self.tokenizer.process(news_content)
        news.set_tokenized(True)
        news.set_params({'headline_tokenized': news_headline_tokenized, 'content_tokenized': news_content_tokenized})



class NewsSentimentAnalysis:
    def process(self, news: News, sentiment_model: str):
        """
        This function should analyze the sentiment of the news.
        Take the headline setense and content sentence and analyze the sentiment of each sentence.
        :param news: News class
        :param sentiment_model: sentiment model to use - just use McDonald for now
        """

        news_headline = news.get_params()['headline']
        news_content = news.get_params()['content']
        sen_model = SentenceSentimentAnalysis()
        news_headline_sentiment = sen_model.process(news_headline, sentiment_model)
        news_content_sentiment = sen_model.process(news_content, sentiment_model)
        news.set_sentiment_analyzed(True)
        news.set_sentiment({'headline': news_headline_sentiment, 'content': news_content_sentiment})


class SentenceSentimentAnalysis:
    def process(self, sentence: Optional[str],sentence_tokenized: Optional[List[str]],
                sentiment_model: str = 'mcdonald'):
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
        pass



class Counter:
    @classmethod
    def run_tokens(cls, tokens: list[str]) -> dict:
        """
        Count the token frequency and return the result as a dictionary.
        :param tokens: list[str]: e.g. ['test', 'sentence', 'sentence', 'SPY', 'great']
        :return: dict , e.g. {'test': 1, 'sentence': 2, 'SPY': 1, 'great': 1}
        """
        pass

    @classmethod
    def run_list_of_tokens(cls, list_of_token: list[str]) -> dict:
        """
        Count the token frequency and return the result as a dictionary.
        :param list_of_token: list[list[str]]: e.g. [['test', 'sentence'], ['sentence', 'SPY'], ['SPY', 'great']]
        :return: List[dict] , e.g. [{'test': 1, 'sentence': 1}, {'sentence': 1, 'SPY': 1}, {'SPY': 1, 'great': 1}]
        """
        pass

class SentenceSpliter:
    def process(self, text: str) -> List[str]:
        """
        This function should split the text into sentences.
        :param text: str
        :return: List[str]
        """
        pass