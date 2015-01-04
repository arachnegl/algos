"""
Linked List implementation
"""
import unittest

class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            cursor = self.head
            while cursor.next:
                # iterate to end of list
                cursor = cursor.next
            cursor.next = Node(value)

    def insert(self, value):
        if self.is_empty():
            self.head = Node(value)
            return
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def count(self):
        if self.is_empty():
            return 0
        cursor = self.head
        count = 1
        while cursor.next:
            cursor = cursor.next
            count += 1
        return count

    def search(self, value):

        if self.is_empty():
            return False

        cursor = self.head

        def found():
            return cursor.value == value

        if found():
            return cursor

        while cursor.next:
            if found():
                return cursor
            cursor = cursor.next
        return False

    def remove(self, value):

        if self.is_empty():
            return False

        # special treatment for first value
        # TODO find algorithm that avoids this
        if self.head.value == value:
            self.head = None
            return True

        assert self.count() > 1, 'list has at least one element'
        found = False
        current = self.head
        previous = None

        while not found:
            if current.value == value:
                found = True
                break
            elif not current.next:
                break
            previous = current
            current = current.next

        if not found:
            return False

        previous.next = current.next
        # current is garbage collected
        return True

    def is_empty(self):
        return not bool(self.head)


class TestLinkedList(unittest.TestCase):

    def test_creation_returns_empty_list(self):

        list_ = LinkedList()

        self.assertTrue(list_.is_empty)

    def test_one_value(self):

        list_ = LinkedList()
        list_.append(1)

        self.assertTrue(isinstance(list_.head, Node))
        self.assertEqual(list_.head.value, 1)
        self.assertFalse(list_.is_empty())

    def test_two_nodes(self):

        list_ = LinkedList()
        list_.append(1)
        list_.append(2)

        self.assertEqual(list_.head.next.value, 2)

    def test_three_nodes(self):

        list_ = LinkedList()
        list_.append(1)
        list_.append(2)
        list_.append(3)

        self.assertEqual(list_.head.next.next.value, 3)

    def test_insert_empty(self):

        list_ = LinkedList()
        list_.insert(1)

        self.assertEqual(list_.head.value, 1)

    def test_insert_one_member(self):

        list_ = LinkedList()
        list_.append(1)
        list_.insert(2)

        self.assertEqual(list_.head.value, 2)
        self.assertEqual(list_.head.next.value, 1)

    def test_insert_two_members(self):

        list_ = LinkedList()
        list_.append(1)
        list_.insert(2)
        list_.insert(3)

        self.assertEqual(list_.head.next.next.value, 1)
        self.assertEqual(list_.head.next.value, 2)
        self.assertEqual(list_.head.value, 3)

    def test_count_empty(self):

        list_ = LinkedList()

        self.assertEqual(list_.count(), 0)

    def test_count_one_member(self):

        list_ = LinkedList()
        list_.insert(2)

        self.assertEqual(list_.count(), 1)

    def test_count_hundred_members(self):

        list_ = LinkedList()
        for i in range(100):
            list_.insert(i)

        self.assertEqual(list_.count(), 100)

    def test_search_empty(self):

        list_ = LinkedList()
        got = list_.search(3)

        self.assertFalse(got)

    def test_search_one_member_true(self):

        list_ = LinkedList()
        list_.insert(3)

        got = list_.search(3)

        self.assertTrue(got)
        self.assertEqual(got.value, 3)

    def test_search_one_member_false(self):

        list_ = LinkedList()
        list_.insert(2)

        got = list_.search(3)

        self.assertFalse(got)

    def test_search_fifty_members_true(self):

        list_ = LinkedList()
        for i in range(50):
            list_.insert(i)

        got = list_.search(49)

        self.assertTrue(got)
        self.assertEqual(got.value, 49)

    def test_search_fifty_members_false(self):

        list_ = LinkedList()
        for i in range(50):
            list_.insert(i)

        got = list_.search(50)

        self.assertFalse(got)

    def test_remove_empty_list(self):

        list_ = LinkedList()

        self.assertFalse(list_.remove(5))

    def test_remove_from_one_member_list(self):

        list_ = LinkedList()
        list_.insert(5)

        list_.remove(5)

        self.assertTrue(list_.is_empty())

    def test_remove_from_two_member_list(self):

        list_ = LinkedList()
        list_.insert(5)
        list_.insert(65)

        list_.remove(5)

        self.assertEqual(list_.count(), 1)
        self.assertEqual(list_.head.value, 65)

    def test_remove_from_end_of_three_member_list(self):

        list_ = LinkedList()
        list_.insert(5)
        list_.insert(65)
        list_.insert(43)

        list_.remove(5)  # first inserted will be last in list

        self.assertEqual(list_.count(), 2)
        self.assertEqual(list_.head.value, 43)
        self.assertEqual(list_.head.next.value, 65)
        self.assertIsNone(list_.head.next.next)

if __name__ == '__main__':
    unittest.main()
