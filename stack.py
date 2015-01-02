"""
Stack implementation and related uses.

Run tests:
    python3 -m unittest stack.py
"""
import unittest


class Stack:

    def __init__(self):
        self.items = list()

    def is_empty(self):
        return bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_balanced(string, opening='({[', closing=']})'):
    """
    test if a string contains a balanced number of
    opening and closing symbols
    """

    stack = list()

    for char in string:
        if char in opening:
            stack.append(opening)
        elif char in closing:
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
            '()', '[]', '{}',
            '(())', '[[]]', '{{}}',
            '((()()))', '[[[][]]]', '{{{}{}}}',
            '{{ ( ) [] () }}', '( [] {} () )',
            'awef ( ) awef', '(awef) (awef)', '((awef) (awef)) ( awef)',
        ]

        self._assert(True, strings)

    def test_basic_imbalanced(self):

        strings = [
            '((', '()))', '(((())',
            '[[[', '[[][]', '{{}', '}}}}}',
            '{{ () [] }',
        ]

        self._assert(False, strings)
