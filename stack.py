import unittest


def is_balanced(string, openclose='()'):
    """
    test if a string contains a balanced number of
    opening and closing symbols
    """

    stack = list()

    opening = openclose[0]
    closing = openclose[1]

    for char in string:
        if char == opening:
            stack.append(opening)
        elif char == closing:
            if not stack:
                # should not be empty at this point
                return False
            stack.pop()
        else:
            continue

    if stack:
        return False
    else:
        return True


class BalancedParenthesisTest(unittest.TestCase):

    def _assert(self, bool_, strings):

        if bool_:
            assertion = getattr(self, 'assertTrue')
        else:
            assertion = getattr(self, 'assertFalse')

        for string in strings:
            got = is_balanced(string)
            assertion(got, msg="Error for '{}'".format(string))

    def test_basic_balanced(self):

        strings = [
            '()', '(())', '((()()))',
            'awef ( ) awef', '(awef) (awef)', '((awef) (awef)) ( awef)',
        ]

        self._assert(True, strings)

    def test_basic_imbalanced(self):

        strings = [
            '((', '()))', '(((())',
        ]

        self._assert(False, strings)
