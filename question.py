import abc

class Question(metaclass=abc.ABCMeta):
    """classe abstraite representant une question"""
    
    def __init__(self,enonce):
        """"constructeur"""
        self.enonce = enonce

    def __str__(self):
        """ tostring"""
        return "{0}".format(self.enonce)

    @abc.abstractmethod
    def IsCorrectAnswer(self,proposition):
        pass

    @abc.abstractmethod
    def getPropositions(self):
        pass
