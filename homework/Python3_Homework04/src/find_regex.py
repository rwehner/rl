"""
Python 3, Homework 04
Find the start/end positions of the phrase
"Regular Expressions" in the given text.
"""
import re

def find_start_end(pattern, text):
    """
    Find the start and end offsets of pattern (a
    valid Python regex) with text (a string).
    Returns a tuple (start, end) if the pattern was found
    and None if it was not.
    """
    m = re.search(pattern, text)
    if m:
        return (m.span())
    return None

if __name__ == "__main__":
    text = 'In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.'
    pattern = 'Regular\sExpressions'
    print(find_start_end(pattern, text))