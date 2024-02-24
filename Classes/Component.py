class News:
    def __init__(self, params=None):
        self.params = params
        self.sentiment = {}
        self.counter = None
        self.count_result = None
        self._is_tokenized = False
        self._is_sentiment_analyzed = False

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

    def set_params(self, param: dict):
        self.params = self.params.update(param)

    def set_sentiment(self, param):
        self.sentiment = self.sentiment.update(param)
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
