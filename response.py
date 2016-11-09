from question import *

class Response:
    """reponse à une question"""

    def __init__(self,question,proposition):
        """constructeur d'une reponse"""
        self.question=question
        self.proposition=proposition
        self.correct=question.IsCorrectAnswer(proposition)

    def __str__(self):
        return "question = {0}, proposition = {1}, correct = {2}".format(self.question, self.proposition,self.correct)

    
            
    
