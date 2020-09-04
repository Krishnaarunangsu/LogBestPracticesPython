"""
MyExample.py
"""

import sys
import os

import constants


class MyExample:
    def __init__(self) -> object:
        self.someValueOne = constants.MY_CONSTANT_ONE + 1
        self.someValueTwo = constants.MY_CONSTANT_TWO + 1


if __name__ == '__main__':
    x = MyExample()
    print(x.someValueOne)
