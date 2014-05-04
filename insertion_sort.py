"""
Implementation of Insertion Sort as found in 'Introduction to Algorithms'
chapter 2

"""
import unittest


def sort(i):
    return i


class TestInsertionSort(unittest.TestCase):

    def test_can_sort_empty_list(self):

        input_ = []

        got = sort(input_)
        output= []

        self.assertSequenceEqual(got, output)
