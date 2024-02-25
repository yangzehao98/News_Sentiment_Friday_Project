class SimpleRelavanceCalculator:
    """
    Relevance = (X-Y)/X
    with X= Total sentences; Y = Location of First Mention
    """

    @classmethod
    def calcualte_relevance(cls, total_sentence_number, location_of_first_mention):
        if location_of_first_mention is None:
            return 0
        X = total_sentence_number
        Y = location_of_first_mention
        return (X-Y)/X