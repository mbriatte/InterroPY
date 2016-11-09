from question import *

class EvalQuestion(Question):
    """classe concrete heritant de Question"""
    """elle part du principe que l'enonce peut etre evaluée"""
    #il faut verifier que la question est evaluable

    def IsCorrectAnswer(self,proposition):
        """valide si la reponse est correcte"""
        return eval("{0}=={1}".format(self.enonce,proposition))

    def getPropositions(self):
        """retourne la la liste des propositions """
        #il n'y apas de proposition pour une evalquestion
        return [] 
        

