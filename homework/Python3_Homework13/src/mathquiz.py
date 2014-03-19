from datetime import datetime
from random import randint

class simpleSumQuestion:
    '''
    Basic container that can ask a simple 2-addend sum question,
    collect an answer, track how long (in seconds) it took
    to collect that answer, and determine if the answer is correct
    '''
    def __init__(self, addend1, addend2, ask_function=input):
        '''
        Requires two integer arguments. The ask_function must be a callable
        that takes a string (self.question) as its only argument, and returns a string 
        that can be coerced into an int and used to set self.given_answer. 
        Intended to absract out the exact method of asking a question from this class.
        '''
        self.addends = ( addend1, addend2 )
        self.correct_answer = sum(self.addends)
        self.question = "What is the sum of %s and %s? " % self.addends
        self.ask_function = ask_function
        self.given_answer = None
        self.duration = None
        self.response_short = None
        
    def ask(self):
        """
        Call the ask_function and time the duration until
        a response is gotten
        """
        start = datetime.now()
        self.given_answer = int(self.ask_function(self.question))
        elapsed = datetime.now() - start
        self.duration = elapsed.seconds
        self.has_correct_answer()
        
    def has_correct_answer(self):
        '''
        check the answer. Set self.response_short
        then return True/False
        '''
        if self.correct_answer == self.given_answer:
            self.response_short = 'right'
            return True
        else:
            self.response_short = 'wrong'
            return False
    
    def get_response(self):
        '''
        return a string indicating if the question
        was answered correctly. If the question has not
        been answered, say so.
        '''
        return "{0} is {1}!".format(self.given_answer, self.response_short)
          
        
def get_addends(low=1, high=10, length=2):
    '''
    returns a tuple containing length random
    integers between low and high, inclusive.
    '''
    result = []
    count=0
    while count < length:
        result.append(randint(low,high))
        count += 1
    return tuple(result)

if __name__ == "__main__":
    questions = 5
    count = 0
    results = []
    
    while count < questions:
        addends = get_addends()
        q = simpleSumQuestion(addends[0], addends[1])
        q.ask()
        print(q.get_response())
        results.append((q.response_short, q.duration))
        count += 1
    
    total_duration = 0    
    for index, result in enumerate(results, 1):
        right_wrong, elapsed_seconds = result
        total_duration += elapsed_seconds
        print('Question #{0} took about {1} seconds to complete and was {2}.'.format(index, elapsed_seconds, right_wrong))
        
    print('You took {0} seconds to finish the quiz'.format(total_duration))
    print('Your average time was {0:.3} seconds per question'.format(total_duration/questions))