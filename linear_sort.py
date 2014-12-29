"""
Implementation of Insertion Sort as found in 'Introduction to Algorithms'
chapter 2

to run tests execute:
    python3 -m unittest linear_sort
"""
import unittest


def insertion_sort(sequence, debug=False):
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


def selection_sort(sequence, debug=False):

    for i, el in enumerate(sequence):
        if debug: print(str(sequence))
        minimum = i
        for j, el in enumerate(sequence[i:]):
            if el < sequence[minimum]:
                minimum = i + j  # new minimum
        # swap values:
        sequence[i], sequence[minimum] = sequence[minimum], sequence[i]

    return sequence


def merge(first, second):
    """
    takes two sorted lists and returns
    them merged into new sorted list
    """
    merged = list()

    i = 0
    y = 0
    while len(first[i:]) and len(second[y:]):
        first_head = first[i]
        second_head = second[y]
        if first_head <= second_head:
            to_add = first_head
            i += 1
        else:
            to_add = second_head
            y += 1
        merged.append(to_add)

    if len(first[i:]):
        merged.extend(first[i:])
    elif len(second[y:]):
        merged.extend(second[y:])
    return merged


def merge_sort(sequence):

    to_merge = [[item] for item in sequence]

    while len(to_merge) > 1:
        first = to_merge[0]
        second = to_merge[1]
        merged = merge(first, second)
        to_merge = to_merge[2:]
        to_merge.append(merged)

    result = to_merge[0]
    return result


class TestInsertionSort(unittest.TestCase):

    # TODO generalise these tests to all sorting algorithms
    # sorts = [insertion_sort, selection_sort]

    def test_can_sort_empty_list(self):

        input_ = []

        output = insertion_sort(input_)
        expected = []

        self.assertSequenceEqual(output, expected)

    def test_can_sort_list_of_length_one(self):

        input_ = [1]

        output = insertion_sort(input_)
        expected = [1]

        self.assertSequenceEqual(output, expected)

    def test_can_sort_ordered_list_of_length_two(self):

        input_ = [1, 2]

        output = insertion_sort(input_)
        expected = [1, 2]

        self.assertSequenceEqual(output, expected)

    def test_can_sort_unordered_list_of_length_two(self):

        input_ = [2, 1]

        output = insertion_sort(input_)
        expected = [1, 2]

        self.assertSequenceEqual(output, expected)

    def test_can_sort_unordered_list_of_length_three(self):

        input_ = [4, 2, 1]

        output = insertion_sort(input_)
        expected = [1, 2, 4]

        self.assertSequenceEqual(output, expected)

    def test_can_sort_unordered_list_of_length_four(self):

        input_ = [4, 2, 1, 3]

        output = insertion_sort(input_)
        expected = [1, 2, 3, 4]

        self.assertSequenceEqual(output, expected)

    def test_can_sort_unordered_list(self):

        input_ = [11, 4, 2, 1, 3, 9]

        output = insertion_sort(input_)
        expected = [1, 2, 3, 4, 9, 11]

        self.assertSequenceEqual(output, expected)


class TestSelectionSort(unittest.TestCase):

    def test_sequence_three_ints(self):

        seq = [1, 3, 2]

        got = selection_sort(seq)
        expected = [1, 2, 3]

        self.assertSequenceEqual(got, expected)

    def test_sequence_four_ints(self):

        seq = [1, 5, 3, 2]

        got = selection_sort(seq)
        expected = [1, 2, 3, 5]

        self.assertSequenceEqual(got, expected)

    def test_sequence_five_ints(self):

        seq = [6, 5, 3, 2, -4]

        got = selection_sort(seq)
        expected = [-4, 2, 3, 5, 6]

        self.assertSequenceEqual(got, expected)


class TestMergeSort(unittest.TestCase):

    def test_merge_three_items_each(self):

        seq_a = [2, 4, 6]
        seq_b = [1, 3, 5]

        got = merge(seq_a, seq_b)
        expected = [1, 2, 3, 4, 5, 6]

        self.assertSequenceEqual(got, expected)

    def test_merge_one_items_each(self):

        seq_a = [2]
        seq_b = [1]

        got = merge(seq_a, seq_b)
        expected = [1, 2]

        self.assertSequenceEqual(got, expected)

    def test_merge_one_items_each_values_swapped(self):

        seq_a = [1]
        seq_b = [2]

        got = merge(seq_a, seq_b)
        expected = [1, 2]

        self.assertSequenceEqual(got, expected)

    def test_merge_sort(self):

        seq = [2, 4, 6, 1, 3, 5]

        got = merge_sort(seq)
        expected = [1, 2, 3, 4, 5, 6]

        self.assertSequenceEqual(got, expected)
