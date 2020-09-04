import unittest
import unittest2


def add(x: int, y: int):
    """
    It adds two numbers
    :param x:
    :param y:
    :return:
    """
    return(x+y)


class SimpleTest(unittest.TestCase):
    """
    Class for Unit Testing
    """
    def test_add(self):
        """
        It tests the method 'add(x, y)'
        :return:
        """
        self.assertEquals(add(4, 5), 9)


if __name__ == '__main__':
    unittest.main()
