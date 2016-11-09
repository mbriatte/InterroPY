from response import *
from user import *
from questionFactory import *
from package.persistance import *

class Session:
    """classe session"""
    #lors d'une session, un membre repond aux questions d'un questionnaire

    def __init__(self,user):
        """constructeur d'une reponse"""
        self.member=user.name
        self.filename=user.questionnaire
        self.reponses=dict()
        self.reponsebonne=0
        self.nbquestion=0
        self.questions=list()
        self.__loadQuestions(self.filename)
      
    def __str__(self):
        return "questionnaire = {0}, membre = {1}, reponses = {2}".format(self.filename, self.member,self.reponses)

    def ajouterReponse(self, question, reponse):
        """ajouter une reponse à une question du questionnaire"""
        self.reponses[question]=reponse
        self.__majnote(reponse)
        # il faudrait ne pas autoriser l'(ajout si une reponse a deja etait faite sur une question
        # il faut verifier que la question fait parie de la liste des question du formulaire
 
    def __majnote(self, reponse):
        """verifie que la reponse est OK"""
        self.nbquestion+=1
        if reponse.correct: self.reponsebonne+=1

    def getnote(self):
        """retourne la note"""
        return "note={0}/{1}".format(self.reponsebonne,self.nbquestion)

    def __loadQuestions(self,filename):
        """charge la liste des questions à partir du fichier"""
        listenonce=getQuestionnaire(filename)
        for elt in listenonce:
            quest=QuestionFactory.create_question(elt)
            self.questions.append(quest)
        
    def saveSession(self):
        """stocke la session sdans un fichier"""
        lesreponses=list()
        for rep in self.reponses.values():
            lesreponses.append(rep)
        saveSession(lesreponses,self.member)
      

        
            
    
