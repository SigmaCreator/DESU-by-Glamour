class GrammarException(Exception):

    def __init__(self,info):

        self.info = info

class EndOfSentenceException(Exception):

    def __init__(self,info):

        self.info = info