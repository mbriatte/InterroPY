import unittest
from questionFactory import *
from response import *
from session import *
from user import *

class SessionTest(unittest.TestCase):
    """ test case d ela classe Session"""

    def test_session_1(self):
        """ test de l'ajout d'une reponse à la session """
        u=User("michael","fichier")
        s=Session(u)
        q=QuestionFactory.create_question("1+2")
        rok=Response(q,3)
        rko=Response(q,4)
        s.ajouterReponse(q,rok)
        s.ajouterReponse(q,rko)
        self.assertTrue(s.nbquestion==2)
        self.assertTrue(s.reponsebonne==1)

    def test_session_2(self):
        """ test du chargement des questions"""
       
        u=User("michael","question1")
        s=Session(u)
        self.assertTrue(len(s.questions)==2)
        self.assertIsInstance(s.questions[0],EvalQuestion)

    def test_session_3(self):
        """ test de la sauvegarde des reponses"""
        u=User("michael","question1")
        s=Session(u)
        q1=s.questions[0]
        self.assertIsInstance(q1,EvalQuestion)
        q2=s.questions[1]
        self.assertIsInstance(q2,QuestionWithResponse)
        r1=Response(q1,3)
        r2=Response(q2,"Hollande")
        s.ajouterReponse(q1,r1)
        s.ajouterReponse(q2,r2)
        s.saveSession()
        
