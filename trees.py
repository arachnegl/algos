#!/usr/bin/env python3
"""
To run with tests:
    python3 -m unittest trees.py

"""

import unittest


class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if not self.left:
            self.left = BinaryTree(value)
        else:
            # push existing node down one level
            tree = BinaryTree(value)
            tree.left = self.left
            self.left = tree

    def insert_right(self, value):
        if not self.right:
            self.right = BinaryTree(value)
        else:
            # push existing node down one level
            tree = BinaryTree(value)
            tree.right = self.right
            self.right = tree


class TestBinaryTree(unittest.TestCase):

    def test_can_create(self):

        tree = BinaryTree(0)

        assert tree.value == 0

    def test_insert_left(self):

        tree = BinaryTree(0)

        tree.insert_left(1)
        tree.left.insert_left(2)
        tree.left.left.insert_left(3)

        assert tree.left.value == 1
        assert tree.left.left.value == 2
        assert tree.left.left.left.value == 3

    def test_insert_left_pushes_down_values(self):

        tree = BinaryTree(0)

        tree.insert_left(1)
        tree.insert_left(2)
        tree.insert_left(3)

        assert tree.left.value == 3
        assert tree.left.left.value == 2
        assert tree.left.left.left.value == 1

    def test_insert_right(self):

        tree = BinaryTree(0)

        tree.insert_right(1)
        tree.right.insert_right(2)
        tree.right.right.insert_right(3)

        assert tree.right.value == 1
        assert tree.right.right.value == 2
        assert tree.right.right.right.value == 3

    def test_insert_right_pushes_down_values(self):

        tree = BinaryTree(0)

        tree.insert_right(1)
        tree.insert_right(2)
        tree.insert_right(3)

        assert tree.right.value == 3
        assert tree.right.right.value == 2
        assert tree.right.right.right.value == 1

    def test_full_binary_tree(self):

        # represent the following binary tree

        #         a
        #       /   \
        #      b     c
        #      \     | \
        #       d    e  f

        tree = BinaryTree('a')

        tree.insert_left('b')
        tree.left.insert_right('d')
        tree.insert_right('f')
        tree.insert_right('c')   # push down 'f'
        tree.right.insert_left('e')

        # assertions in breadth first search order
        assert tree.value == 'a'

        assert tree.left.value == 'b'
        assert tree.right.value == 'c'

        assert tree.left.right.value == 'd'
        assert tree.right.left.value == 'e'
        assert tree.right.right.value == 'f'
