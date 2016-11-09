# -*-coding:Latin-1 -*

import os

def __loadliste(fichier):
    os.chdir("D:/python/questionnaire")
    fichier=open(fichier+".txt","r")
    contenu=list()
    continuer=True
    while continuer:
        ligne=fichier.readline()
        if len(ligne)>0:
            #il faut supprimer le dernier caracretere qui est '\n'
            if ligne[-1]=='\n': ligne=ligne[0:len(ligne)-1]
            contenu.append(ligne)
        else:
            continuer=False
    fichier.close()
    return contenu

def __saveliste(pliste,fichier):
    os.chdir("D:/python/questionnaire")
    liste=list(pliste)
    fichier=open(fichier+".txt","a")
    for elt in liste:
        fichier.writelines(str(elt)+'\n')
    fichier.close()

def getQuestionnaire(fichier):
    return __loadliste(fichier)

def getusers(fichier):
    return __loadliste(fichier)

def saveSession(pliste,fichier):
    __saveliste(pliste,fichier)

