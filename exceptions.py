class GrammarException(Exception):

    def __init___(self,dErrorArguments):

        Exception.__init__(self,"my exception was raised with arguments {0}".format(dErrArguments))

        self.dErrorArguments = dErrorArguements

class EndOfSentenceException(Exception):

    def __init___(self,dErrorArguments):

        Exception.__init__(self,"my exception was raised with arguments {0}".format(dErrArguments))

        self.dErrorArguments = dErrorArguements