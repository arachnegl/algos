"""
Implementation of Insertion Sort as found in 'Introduction to Algorithms'
chapter 2
"""
import unittest


def sort(a):
    """ Sorts sequence using insertion sort algorithm
    """
    for j, el in enumerate(a):
        if j == 0:
            continue
        key = a[j]
        # insert A[j] into sorted sequence A[1..j-1]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a


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

    def test_can_sort_ordered_list_of_length_two(self):

        input_ = [1, 2]

        output = sort(input_)
        expected = [1, 2]

        self.assertSequenceEqual(output, expected)

    def test_can_sort_unordered_list_of_length_two(self):

        input_ = [2, 1]

        output = sort(input_)
        expected = [1, 2]

        self.assertSequenceEqual(output, expected)

    def test_can_sort_unordered_list_of_length_three(self):

        input_ = [4, 2, 1]

        output = sort(input_)
        expected = [1, 2, 4]

        self.assertSequenceEqual(output, expected)

    def test_can_sort_unordered_list_of_length_four(self):

        input_ = [4, 2, 1, 3]

        output = sort(input_)
        expected = [1, 2, 3, 4]

        self.assertSequenceEqual(output, expected)
