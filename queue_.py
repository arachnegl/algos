"""
Implementation of the Queue ADT

Methods:
    Queue()         - constructor, creates new empty queue
    enqueue(item)   - add item to rear of queue, returns nothing
    dequeue()       - remove and returns item from front of queue
    is_empty()
    size()

Run tests
    python3 queue.py
"""
import unittest


class Queue:

    def __init__(self):
        self.size = 0
        self.queue = list()

    def enqueue(self, item):
        self.size += 1
        self.queue.insert(0, item)

    def dequeue(self):
        assert self.size >= 0
        if not self.size:
            return None
        self.size -= 1
        assert self.size >= 0
        return self.queue.pop()

    def is_empty(self):
        return not bool(self.size)


def hot_potato(names, number):

    assert number > 0, 'number argument must be positive non zero int'
    assert len(names) > 0, 'need at least one name'

    simulation = Queue()
    for name in names:
        simulation.enqueue(name)

    while simulation.size > 1:
        for _ in range(number):
            # take from front and requeue at back
            simulation.enqueue(
                simulation.dequeue()
            )
        # remove the hot potato
        simulation.dequeue()

    assert simulation.size == 1, 'One left invariant'
    return simulation.dequeue()

class TestQueue(unittest.TestCase):

    def test_create_empty_instance(self):

        q = Queue()

        self.assertIsInstance(q, Queue)

    def test_enqueue(self):

        q = Queue()
        q.enqueue(4)

        self.assertEqual(q.size, 1)

    def test_enqueue_two_items(self):

        q = Queue()
        q.enqueue(1)
        q.enqueue(2)

        self.assertEqual(q.size, 2)

    def test_dequeue_empty(self):

        q = Queue()
        got = q.dequeue()

        self.assertIsNone(got)

    def test_dequeue_non_empty(self):

        queue = Queue()
        queue.enqueue(1)
        got = queue.dequeue()

        self.assertEqual(got, 1)
        self.assertEqual(queue.size, 0)

    def test_dequeue_two_FIFO(self):

        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        got = q.dequeue(), q.dequeue()

        self.assertEqual(got, (1, 2))

    def test_dequeue_four_FIFO(self):

        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        dequeue = q.dequeue

        got = tuple(map(lambda f: f(), [dequeue] * 4))

        self.assertEqual(got, (1, 2, 3, 4))

    def test_empty_is_empty(self):

        queue = Queue()

        self.assertTrue(queue.is_empty())

    def test_not_empty_is_not_empty(self):

        queue = Queue()
        queue.enqueue(1)

        self.assertFalse(queue.is_empty())


class TestHotPotatoSimulation(unittest.TestCase):

    def test_two_players_with_2(self):

        names = ['naomi', 'greg']
        got = hot_potato(names, 2)

        self.assertEqual(got, 'greg')

    def test_three_players_with_1(self):

        names = ['naomi', 'greg', 'angela']
        got = hot_potato(names, 1)

        self.assertEqual(got, 'angela')

    def test_full_game(self):

        names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
        got = hot_potato(names, 7)

        self.assertEqual(got, 'Susan')


if __name__ == '__main__':
    unittest.main()
