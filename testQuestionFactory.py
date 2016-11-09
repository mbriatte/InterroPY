import unittest
from questionFactory import *

class QuestionFactoryTest(unittest.TestCase):
    """test Case de de la classe QuestionFactory"""

    def test_createeval(self):
        """ test de la factory poru création d'une evalquestion"""
        q=QuestionFactory.create_question("1+2")
        self.assertIsInstance(q,EvalQuestion)

    def test_createquestionwithResponse(self):
        """ test de la factory poru création d'une QuestionWithResponse"""
        q=QuestionFactory.create_question("qui est le president de la république française en 2015#François Hollande")
        self.assertIsInstance(q,QuestionWithResponse)

    def test_createquestionwithPoposition(self):
        """ test de la factory poru création d'une QuestionWithResponse"""
        q=QuestionFactory.create_question("qui est le president de la république française en 2015#François Hollande#Chirac#Sarko")
        self.assertIsInstance(q,QuestionWithResponse)
        self.assertTrue(len(q.choix)==3)

        
    
