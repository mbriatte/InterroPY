import unittest
from user import *

class UserTest(unittest.TestCase):
    """ test case de la classe user"""

    def test_getusers(self):
        """test de la methode getusers qui charge la luste des users"""
        q=User.getusers()
        self.assertTrue(len(q)==2)
        self.assertIsInstance(q[0],User)
        self.assertTrue(q[0].name=="Romain")
        self.assertTrue(q[0].questionnaire=="question1")
    
