import unittest


def int_hash_function(an_int, size):
    index = an_int % size
    return index


class MyDict(object):

    def __init__(self, size=10):
        self.size = size
        self._array = [None] * size

    def my_set(self, key, val):
        index = int_hash_function(key, self.size)
        self._array[index] = val

    def my_get(self, key):
        index = int_hash_function(key, self.size)
        return self._array[index]

    def my_in(self, val):
        for existing_val in self._array:
            if val == existing_val:
                return True
        return False


class TestHashTable(unittest.TestCase):

    def test_can_hash_integer(self):

        got = int_hash_function(0, 10)

        assert got == 0

    def test_can_use_int_as_key(self):

        a_dict = MyDict()

        got = a_dict.my_get(4)

        assert got == None

        a_dict.my_set(4, 4)
        got = a_dict.my_get(4)

        assert got == 4

        a_dict.my_set(4, 5)
        got = a_dict.my_get(4)

        assert got == 5
