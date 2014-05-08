"""
Implementation of Insertion Sort as found in 'Introduction to Algorithms'
chapter 2

"""
import unittest


def sort(a, debug=False):
    """ Sorts sequence using insertion sort algorithm

    I: sequence of numbers <a1, ... , an>
    O: permutation <a1', ... , an'> such that a1' <= .... <= an'

    sorting is in palce think two subarrays:
        A[1 .. j -1] is sorted
        A[j + 1 .. n] is unsorted
    """
    for j, el in enumerate(a):
        if j == 0:
            continue
        key = a[j]
        # insert A[j] into sorted sequence A[1..j-1]
        i = j - 1
        # a[0:i] is the ordered subarray
        # a[i:len(a)] is unordered subarray
        while i >= 0 and a[i] > key:
            # this iterates down the ordered subarray
            # 'pushing up' values to create space for
            # right location for the key
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
        if debug:
            print str(a)
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
