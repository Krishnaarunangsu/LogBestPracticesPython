class Test:
    def __init__(self):
        """
        Initialize variables
        """
        self.str="geeksforgeeks"
        self.x=20

def fun():
    return Test()

test = fun()
print('String Value:{}'.format(test.str))
print('Integer Value:{}'.format(test.x))
print(test.str)


