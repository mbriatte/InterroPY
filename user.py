from package.persistance import *

class User:

    users=list()
    isloaded=False
   
    def __init__(self,name,questionnaire):
        """constructeur de user"""
        self.name=name
        self.questionnaire=questionnaire

    def __str__(self):
        return "nom={0}, questionnaire={1}".format(self.name,self.questionnaire)

    def __loadusers(cls):
        """methode privée de chargement des users"""
        cls.liste=getusers("users")
        cls.isloaded=True
        for elt in cls.liste:
            tokens=elt.split(";")
            nouveauUtilisateur=User(tokens[0],tokens[1])
            cls.users.append(nouveauUtilisateur)

    def getusers(cls):
        """retourne la liste des utilisateyurs"""
        if not cls.isloaded :cls.__loadusers()
        return cls.users
            
    __loadusers=classmethod(__loadusers)
    getusers=classmethod(getusers)

        
        
