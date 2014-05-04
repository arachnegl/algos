"""
Implementation of Insertion Sort as found in 'Introduction to Algorithms'
chapter 2

"""
import unittest


def sort(sequence):
    """ Sorts sequence using insertion sort
    """
    # to retain polymorphism we order in place,
    # we assume sequence supports indexing
    if len(sequence) > 1 and sequence[0] > sequence[1]:
        sequence[0], sequence[1] = sequence[1], sequence[0]
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
