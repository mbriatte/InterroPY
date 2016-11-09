from evalquestion import *
from questionWithResponse import *

class QuestionFactory(object):
    """factory poru créer des questions à partir de leur definition"""
    
    # Create based on definition  split:
    def create_question(definition):
        tokens=definition.split("#")
        if len(tokens) == 1: return EvalQuestion(tokens[0])
        elif len(tokens) >= 2: return QuestionWithResponse(tokens[0],tokens[1], tokens[2:len(tokens)])
        
       
        
      
