from datetime import datetime


class News:
    def __init__(self, params=None):
        self.params = params
        self.sentiment = {}
        self.counter = None
        self.count_result = None
        self._is_tokenized = False
        self._is_sentiment_analyzed = False
        self.date = None


    def run_counter(self):
        from Classes.DataProcessor import Counter
        """
        This function should run the counter. The counter should be able to run after tokenization.
        """

        if not self._is_tokenized:
            raise ValueError('The news is not tokenized yet. Please tokenize the news first.')
        self.count_result = Counter.run(self.params)

    def set_tokenized(self, is_tokenized: bool):
        self._is_tokenized = is_tokenized

    def get_count_results(self) -> dict:
        return self.count_result

    def get_sentiment(self) -> dict[str: dict]:
        if not self._is_sentiment_analyzed:
            raise ValueError('The news is not sentiment analyzed yet. Please analyze the sentiment of the news first.')

        return self.sentiment

    def get_params(self) -> dict:
        return self.params

    def set_sentiment_analyzed(self, is_sentiment_analyzed: bool):
        self._is_sentiment_analyzed = is_sentiment_analyzed

    def get_headline_tokenized(self):
        headline_tokenized = self.params.get('headline_tokenized', None)
        if headline_tokenized is None:
            raise ValueError('The news is not tokenized yet. Please tokenize the news first.')
        return headline_tokenized

    def get_content_tokenized(self):
        content_tokenized = self.params.get('content_tokenized', None)
        if content_tokenized is None:
            raise ValueError('The news is not tokenized yet. Please tokenize the news first.')
        return content_tokenized

    def set_params(self, param: dict):
        self.params.update(param)

    def set_sentiment(self, param):
        self.sentiment.update(param)
    '''
    def to_dict(self):
        # Method to convert the news parameters to dictionary (this is easily JSON serializable)
        return {
            'params': self.params,
            'sentiment': self.sentiment,
            'count_result': self.count_result,
            'is_tokenized': self._is_tokenized,
            'is_sentiment_analyzed': self._is_sentiment_analyzed
        }
    '''

    def get_total_sentiment_counts(self):
        return self.sentiment.get('total_sentiment_counts', None)

    def __str__(self):
        return f'News Object: {self.params}'

    def __repr__(self):
        return f'News Object: {self.params["headline"]}'

    def set_date(self, date: datetime):
        self.date = date

    def get_date(self):
        return self.date



