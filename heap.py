#!/usr/bin/env python3
"""
Heap implementation

Run tests:
    python3 heap.py
"""
import unittest
import copy


class BinaryHeap:

    def __init__(self):
        self.list = [0]  # non empty so that index math works
        self.size = 0

    def percolate_up(self, i):
        max_depth = 1000  # infinite loop guard
        while i // 2 > 0 and max_depth > 0:
            max_depth -= 1
            if self.list[i] < self.list[i // 2]:
                tmp = self.list[i // 2]
                self.list[i // 2] = self.list[i]
                self.list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.list.append(k)
        self.size += 1
        self.percolate_up(self.size)

    def delete_min(self):
        min_ = self.list[1]
        self.list[1] = self.pop()
        self.size -= 1
        self.percolate_down(self.size)
        return min_


class TestHeap(unittest.TestCase):

    def test_creation(self):

        heap = BinaryHeap()

        self.assertIsInstance(heap, BinaryHeap)
        self.assertEqual(heap.list, [0])
        self.assertEqual(heap.size, 0)

    def test_insert_first_number(self):

        heap = BinaryHeap()
        heap.insert(5)

        self.assertEqual(heap.list, [0, 5])
        self.assertEqual(heap.size, 1)

    def test_insert_two_numbers_increasing(self):

        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(7)

        self.assertEqual(heap.list, [0, 5, 7])
        self.assertEqual(heap.size, 2)

    def test_insert_three_numbers_increasing(self):

        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(7)
        heap.insert(8)

        self.assertEqual(heap.list, [0, 5, 7, 8])
        self.assertEqual(heap.size, 3)

    def test_insert_two_numbers_decreasing(self):

        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(3)

        self.assertEqual(heap.list, [0, 3, 5])
        self.assertEqual(heap.size, 2)

    def test_full_example(self):

        initial_heap = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

        heap = BinaryHeap()
        heap.list = copy.copy(initial_heap)
        heap.insert(7)

        expected = [0, 5, 7, 11, 14, 9, 19, 21, 33, 17, 27, 18]

        self.assertEqual(heap.list, expected)
        self.assertEqual(heap.size, len(initial_heap) + 1)


if __name__ == '__main__':
    unittest.main()
