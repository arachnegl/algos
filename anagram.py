"""
Anagram functions

Algorithms with different orders of magnitude
"""
import unittest

from collections import OrderedDict


def anagram_first(first, second):
    """
    Strategy: Tick off
    """

    if first == second:
        return True

    if not len(first) == len(second):
        return False

    for char in first:
        if char in second:
            second = second.replace(char, '-', 1)
            first = first.replace(char, '-', 1)

    def is_hyphens(a_str):
        return all(map(lambda x: x == '-', a_str))

    if is_hyphens(first) and is_hyphens(second):
        return True
    else:
        return False


def anagram_tick_off(first, second):

    first = [char for char in first]

    idx = 0
    ok = True
    while idx < len(first) and ok:
        jdx = 0
        found = False
        while jdx < len(second) and not found:
            if first[idx] == second[jdx]:
                found = True
            else:
                jdx += 1
        if not found:
            ok = False
        idx += 1

    return ok


def anagram_sort_and_compare(first, second):

    if first == second:
        return True
    if not len(first) == len(second):
        return False

    first = list(first)
    second = list(second)

    first.sort()
    second.sort()

    for char_a, char_b in zip(first, second):
        if not char_a == char_b:
            return False
    return True


def anagram_count_and_compare_first(first, second):
    # sacrifice space for time

    if first == second:
        return True
    if not len(first) == len(second):
        return False

    def count_chars(string):
        res = OrderedDict()
        for char in first:
            if char in res:
                res[char] += 1
            else:
                res[char] = 1
        return res

    first_res = count_chars(first)
    second_res = count_chars(second)

    for count_one, count_two in zip(first_res.values(), second_res.values()):
        if not count_one == count_two:
            return False

    return True


def anagram_count_and_compare(first, second):

    # init letter counts
    letter_count_a = [0]*26
    letter_count_b = [0]*26

    for char in first:
        idx = ord(char) - ord('a')
        current = letter_count_a[idx]
        letter_count_a[idx] = current + 1

    for char in second:
        idx = ord(char) - ord('a')
        current = letter_count_b[idx]
        letter_count_b[idx] = current + 1

    for i in range(26):
        if not letter_count_a[i] == letter_count_b[i]:
            return False

    return True


class TestAnagram(unittest.TestCase):

    tests = [
        ('', '', True),             # empty stings
        ('abc', 'abc', True),       # identical strings
        ('abcd', 'abc', False),     # strings of unequal length
        ('heart', 'earth', True),
        ('python', 'typhon', True),
        ('apple', 'pleap', True),
    ]

    @classmethod
    def _wrap(cls, anagram_function):

        def inner():
            for arg1, arg2, res in cls.tests:
                got = anagram_function(arg1, arg2)
                err_msg = '"{}" "{}" failed, expected "{}"'.format(
                    arg1, arg2, res
                )
                assert got == res, err_msg

        return inner

    def test_anagram_first(self):

        self._wrap(anagram_first)()

    def test_anagram_tick_off(self):

        self._wrap(anagram_tick_off)()

    def test_anagram_sort_and_compare(self):

        self._wrap(anagram_sort_and_compare)()

    def test_anagram_count_and_compare_first(self):

        self._wrap(anagram_count_and_compare_first)()

    def test_anagram_count_and_compare(self):

        self._wrap(anagram_count_and_compare)()


if __name__ == '__main__':
    unittest.main()
