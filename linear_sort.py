"""
Implementation of Insertion Sort as found in 'Introduction to Algorithms'
chapter 2

to run tests execute:
    python3 -m unittest insertion_sort
"""
import unittest


def sort(sequence, debug=False):
    """ Sorts sequence using insertion sort algorithm

    I: sequence of numbers <a1, ... , an>
    O: permutation <a1', ... , an'> such that a1' <= .... <= an'

    sorting is in palce think two subarrays:
        A[1 .. j -1] is sorted
        A[j + 1 .. n] is unsorted

    if debug is true state of sequence after each run is printed
    """

    # a[0:i] is the ordered subarray
    # a[i:len(a)] is unordered subarray

    # The while loop iterates down the ordered subarray
    # 'pushing up' values to create space for
    # right location for the key

    # j is index of current element
    # insert A[j] into sorted sequence A[1..j-1]

    for j, el in enumerate(sequence):
        if j == 0: continue
        if debug: print(str(sequence))
        key = sequence[j]
        i = j - 1
        # Descend ordered sequence and whilst
        # cursor element is superior to key
        # shift element at index i to i + 1
        while i >= 0 and sequence[i] > key:
            sequence[i + 1] = sequence[i]
            i = i - 1
        sequence[i + 1] = key  # insert key
    return sequence


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

    def test_can_sort_unordered_list(self):

        input_ = [11, 4, 2, 1, 3, 9]

        output = sort(input_)
        expected = [1, 2, 3, 4, 9, 11]

        self.assertSequenceEqual(output, expected)
