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

        output = sort(input_)
        expected = []

        self.assertSequenceEqual(output, expected)

    def test_can_sort_list_of_length_one(self):

        input_ = [1]

        output = sort(input_)
        expected = [1]

        self.assertSequenceEqual(output, expected)
