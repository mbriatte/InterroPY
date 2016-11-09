from user import *
from session import *


def choisirutilisateur():
    
    users=User.getusers()
    reponse=0
    
    for i,elt in enumerate(users):
        print("{0} => choix {1}".format(elt.name,i))
        
    saisievalide=False
    while (not saisievalide):    
        try :            
            choix=input("choix ? ")
            reponse=int(choix)
            assert reponse>=0 and reponse<len(users)
            saisievalide=True
        except:
             print("le choix doit etre compris entre 0 et {0}".format(len(users)-1))
             saisievalide=False
                   
    return users[reponse]

def questionnerutilisateur(question):
    reponse=input("{0} ? {1}".format( question.enonce,afficherproposition(question.getPropositions())))
    return reponse

def validersaisie(reponse, propositions):
    taille=len(propositions)
    rst=True
    
    if taille>0:
        try:
            valeur=int(reponse)
            assert valeur>=0 and valeur<taille
            rst= True
        except:
            print("le choix doit faire partie des propositions")
            rst=False          
    return rst


def afficherproposition(propositions):
    chaine=""
    for i,elt in enumerate(propositions):
        if i>0:chaine+=" ou "
        chaine+="{0}(choix {1})".format(elt,i)
    return chaine

def traiterquestion(question):
    q=question.enonce
    propositions=question.getPropositions()
    saisieok = False
    while not saisieok:
        saisie=questionnerutilisateur(question)
        saisieok=validersaisie(saisie,propositions)

    reponse=creerreponse(question,saisie)

    return reponse

def creerreponse(question,saisie):
    propositions=question.getPropositions()
    if len(propositions)>0:
        assert int(saisie)>=0
        saisie=propositions[int(saisie)]
    reponse=Response(question,saisie)
    return reponse
    
        
def repondrequestionnaire(user):
    s=Session(user)
    for i,elt in enumerate(s.questions):
        print("Question {0}".format(i+1))
        reponse=traiterquestion(elt)
        s.ajouterReponse(elt,reponse)
    
    return s
        
utilisateur=choisirutilisateur()       
sessionutilisateur=repondrequestionnaire(utilisateur)
print(sessionutilisateur.getnote())
sessionutilisateur.saveSession()
