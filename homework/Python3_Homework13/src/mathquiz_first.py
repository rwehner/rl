from datetime import datetime
from random import randint

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
    count = 0
    questions = 5
    results = []
    
    while count < questions:
        addends = get_addends()
        start = datetime.now()
        answer = input("What is the sum of %s and %s? " % addends)
        duration = datetime.now() - start
        if int(answer) == sum(addends):
            iscorrect = 'right'
        else:
            iscorrect = 'wrong'
        response = "{0} is {1}!".format(answer, iscorrect)
        results.append((iscorrect, duration.seconds))
        count += 1
    
    total_duration = 0    
    for index, result in enumerate(results, 1):
        right_wrong, elapsed_seconds = result
        total_duration += elapsed_seconds
        print('Question #{0} took about {1} seconds to complete and was {2}.'.format(index, elapsed_seconds, right_wrong))
        
    print('You took {0} seconds to finish the quiz'.format(total_duration))
    print('Your average time was {0:.3} seconds per question'.format(total_duration/questions))
    
    