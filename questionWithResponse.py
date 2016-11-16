from question import *

class QuestionWithResponse(Question):
    """classe concrete heritant de Question"""
    """elle part du principe qu'une solution est fournie"""

    def __init__(self,enonce, solution, propositions=[]):
        """"constructeur"""
        Question.__init__(self,enonce)
        self.choix=list()
        #la reponse est mise dans la liste des choix en premiere position
        self.choix.append(solution)
        # les autres proposition si elle existe sont ajoutées à la liste
        self.choix+=(propositions)

    def __str__(self):
        """ tostring"""
        return "{0}=> solutions={1} ".format(self.enonce,self.choix)

    def IsCorrectAnswer(self,proposition):
        """valide si la reponse est correcte en comparant la reponse au premier element de la liste de choix"""
        return self.choix[0]==proposition
    
    def getPropositions(self):
        """retourne la la liste des propositions s'il y  en a a au 2 """
        #l'appel à cette fonction retournera vide  s'il n'y a qu'une proposition ( puisque c'est forcement la reponse :))
        if len(self.choix)==1:
            return [] 
        else:
            return sorted(self.choix)

