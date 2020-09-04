'''
Module showing how doctests can be included with source code
Each '>>>' line is run as if in a python shell, and counts as a test.
The next line, if not '>>>' is the expected output of the previous line.
If anything doesn't match exactly (including trailing spaces), the test fails.
'''

def multiply(a, b):
    """
    >>> multiply(4, 3)
    10
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b

"""
conceptual model of python doctest
This is from python.org:

The doctest module searches for pieces of text that look like interactive Python sessions,
and then executes those sessions to verify that they work exactly as shown
"""
