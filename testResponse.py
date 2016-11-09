import unittest
from questionFactory import *
from response import *

class ResponseTest(unittest.TestCase):
    """ test case de la classe Response"""

    def test_reponseok_pour_evalquestion(self):
        """ test d'une reponse ok à une evalquestion """
        q=QuestionFactory.create_question("1+2")
        r=Response(q,3)
        self.assertTrue(r.correct)

    def test_reponseok_pour_evalquestion2(self):
        """ test d'une reponse ok à une evalquestion """
        q=QuestionFactory.create_question("1+2")
        r=Response(q,"3")
        self.assertTrue(r.correct)

    def test_reponseko_pour_evalquestion(self):
        """ test d'une reponse ko à une evalquestion """
        q=QuestionFactory.create_question("1+2")
        r=Response(q,4)
        self.assertFalse(r.correct)


    def test_reponseko_pour_evalquestion2(self):
        """ test d'une reponse ko à une evalquestion """
        q=QuestionFactory.create_question("1+2")
        r=Response(q,"4")
        self.assertFalse(r.correct)
    
    def test_reponseok_pour_questionwithreponse(self):
        """ test d'une reponse ok à une evalquestion """
        q=QuestionFactory.create_question("qui est Tony Stark#Iron Man#Spiderman#Batman")
        r=Response(q,"Iron Man")
        self.assertTrue(r.correct)

    def test_reponseko_pour_questionwithreponse(self):
        """ test d'une reponse ok à une evalquestion """
        q=QuestionFactory.create_question("qui est Tony Stark#Iron Man#Spiderman#Batman")
        r=Response(q,"Batnan")
        self.assertFalse(r.correct)
