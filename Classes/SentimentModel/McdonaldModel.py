from typing import List

from SingletonSentimentModel import SingletonSentimentModel
class McdonaldModel(metaclass=SingletonSentimentModel):
    def __init__(self):
        self.model = "mcdonald"
    def process(self, sentence_tokenized: List[str]):
        # TODO: Implement the McDonald Model; and return the sentiment dict
        pass


