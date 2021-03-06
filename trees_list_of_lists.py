"""
Representing trees using list of lists

Advantages:
    * Recursive structure matches recursive definition of a tree.
    * Generalises to many children by using a list as second item.

"""
import unittest

from functools import partial


def binary_tree(value):
    return [value, [], []]


def get_value(tree):
    return tree[0]


def set_value(tree, value):
    tree[0] = value


def get_left(tree):
    return tree[1]


def get_right(tree):
    return tree[2]


def insert(index, tree, new_tree):
    if not tree[index]:
        tree[index] = new_tree
    else:
        new_tree[index] = tree[index]
        tree[index] = new_tree
    return new_tree

insert_left = partial(insert, 1)
insert_right = partial(insert, 2)


def traverse(tree):
    """
    Preorder
    """

    left = get_left(tree)
    right = get_right(tree)

    if left:
        left = traverse(left)
    if right:
        right = traverse(right)

    return [get_value(tree), left, right]


class TestListOfListTrees(unittest.TestCase):

    def test_create_binary_tree(self):

        tree = binary_tree(3)

        got = get_value(tree)

        self.assertEqual(got, 3)

    def test_create_binary_tree_children(self):

        tree = binary_tree(3)

        got = get_left(tree)
        self.assertEqual(got, [])
        got = get_right(tree)
        self.assertEqual(got, [])

    def test_insert_left_once(self):

        tree = binary_tree(3)
        insert_left(tree, binary_tree(4))

        left_tree = get_left(tree)

        self.assertEqual(get_value(left_tree), 4)

    def test_insert_left_twice(self):

        tree = binary_tree(3)
        insert_left(tree, binary_tree(4))
        insert_left(tree, binary_tree(5))

        first_level_left = get_left(tree)
        second_level_left = get_left(first_level_left)

        self.assertEqual(get_value(first_level_left), 5)
        self.assertEqual(get_value(second_level_left), 4)

    def test_insert_left_thrice(self):

        tree = binary_tree(3)
        insert_left(tree, binary_tree(4))
        insert_left(tree, binary_tree(5))
        insert_left(tree, binary_tree(6))

        first_level_left = get_left(tree)
        second_level_left = get_left(first_level_left)
        third_level_left = get_left(second_level_left)

        self.assertEqual(get_value(first_level_left), 6)
        self.assertEqual(get_value(second_level_left), 5)
        self.assertEqual(get_value(third_level_left), 4)

    def test_insert_right_once(self):

        tree = binary_tree(3)
        insert_right(tree, binary_tree(4))

        right_tree = get_right(tree)

        self.assertEqual(get_value(right_tree), 4)

    def test_insert_right_twice(self):

        tree = binary_tree(3)
        insert_right(tree, binary_tree(4))
        insert_right(tree, binary_tree(5))

        first_level_right = get_right(tree)
        second_level_right = get_right(first_level_right)

        self.assertEqual(get_value(first_level_right), 5)
        self.assertEqual(get_value(second_level_right), 4)

    def test_insert_right_thrice(self):

        tree = binary_tree(3)
        insert_right(tree, binary_tree(4))
        insert_right(tree, binary_tree(5))
        insert_right(tree, binary_tree(6))

        first_level_right = get_right(tree)
        second_level_right = get_right(first_level_right)
        third_level_right = get_right(second_level_right)

        self.assertEqual(get_value(first_level_right), 6)
        self.assertEqual(get_value(second_level_right), 5)
        self.assertEqual(get_value(third_level_right), 4)


class TestTraversingListOfListTree(unittest.TestCase):

    # root represents this tree:
    #       'a'
    #      /   \
    #    'b'    'c'
    #      \    /  \
    #      'd''e'   'f'

    root = binary_tree('a')
    b = insert_left(root, binary_tree('b'))
    c = insert_right(root, binary_tree('c'))
    insert_right(b, binary_tree('d'))
    insert_left(c, binary_tree('e'))
    insert_right(c, binary_tree('f'))

    def test_fixture(self):

        tree = self.root

        self.assertEqual(get_value(tree), 'a')

    def test_traverse(self):

        tree = self.root
        got = traverse(tree)

        expected = ['a',
                    ['b',
                     [],
                     ['d', [], []]],
                    ['c',
                     ['e', [], []],
                     ['f', [], []]]
                    ]

        self.assertEqual(got, expected)


if __name__ == '__main__':
    unittest.main()
