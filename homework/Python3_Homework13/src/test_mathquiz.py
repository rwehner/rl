import unittest
from time import sleep
from random import randint

from mathquiz import *

def asker(question):
    '''
    Hard-coded ask_function() to allow
    testing of questions without using
    interactive input() and with time delay.
    '''
    sleep(1)
    return '3'

def askerFalse(question):
    '''
    same as above, but return an answer we
    know will be false (given positive integers are used
    in all tests.
    '''
    return '0'
    
class TestMathQuiz(unittest.TestCase):
    'Test the mathquiz module'
    def test_get_addends(self):
        # verify tuple length
        self.assertEqual(len(get_addends()), 2)
        self.assertEqual(len(get_addends(length=3)), 3)
        
        # verify we get integers and in the right range
        result = get_addends(length=1)[0]
        self.assertTrue(isinstance(result, int))
        self.assertTrue(1 <= result <= 10)
        
    def test_simpleSumQuestion(self):
        question = simpleSumQuestion(1,2, ask_function=asker)
        # verify initial state
        self.assertIsNone(question.given_answer)
        self.assertIsNone(question.duration)        
        self.assertEqual(question.correct_answer, 3)
        self.assertEqual(question.question, "What is the sum of 1 and 2? ")
        # ask the question and verify changes
        question.ask()
        self.assertEqual(question.given_answer, 3)
        self.assertTrue(question.duration > 0)
        self.assertTrue(question.has_correct_answer())
        self.assertEqual(question.get_response(), "3 is right!")
        # reset with an incorrect answer
        question = simpleSumQuestion(10,2, ask_function=asker)
        question.ask()
        self.assertFalse(question.has_correct_answer())
        self.assertEqual(question.get_response(), "3 is wrong!")
        
        # This feels a bit forced, but here is some testing using
        # random ints
        question = simpleSumQuestion(randint(1,10), randint(1,10), ask_function=askerFalse)
        question.ask()
        self.assertTrue(isinstance(question.correct_answer, int))
        self.assertFalse(question.has_correct_answer())
        self.assertTrue(question.get_response().endswith("wrong!"))
        
if __name__ == "__main__":
    unittest.main()