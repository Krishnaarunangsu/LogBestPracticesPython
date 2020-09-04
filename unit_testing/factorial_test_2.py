# define a function to test
def factorial(n):
    '''
    This function calculates recursively and
    returns the factorial of a positive number.
    Define input and expected output:
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    '''
    if n <= 1:
        return 1
    return n * factorial(n - 1)

class FactrioalTest:
    """
    Testing Factorial
    """
    def __init__(self):
        """
        Initialization
        """
        self.result=int()

    def factorial_test(n: int):
        '''
        This function calculates recursively and
        returns the factorial of a positive number.
        Define input and expected output:
        >>> factorial(3)
        5
        >>> factorial(5)
        120
        '''
        if n <= 1:
            return 1
        return n * factorial(n - 1)

