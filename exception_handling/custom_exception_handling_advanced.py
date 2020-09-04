# Advanced Custom Exception
class InvalidInputError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

inp = int(input("Enter a number between 1 to 10:"))
try:
    if type(inp) != int or inp not in list(range(1,11)):
        raise InvalidInputError(inp)
except InvalidInputError:
    print("Invalid input entered:{}".format(inp))
