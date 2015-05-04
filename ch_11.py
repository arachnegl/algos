import unittest
from StringIO import StringIO


def find_dups(a_list):
    exists = set()
    duplicates = set()
    for i in a_list:
        if i in exists:
            duplicates.add(i)
        exists.add(i)
    return duplicates


def mating_pairs(males, females):
    """ zip like function """
    males = set(males)
    females = set(females)
    pairs = set()
    for _ in range(len(males)):
        pair = males.pop(), females.pop()
        pairs.add(pair)

    return pairs


def get_authors(pdb_files):
    authors = set()

    for file_ in pdb_files:
        content = file_.read()
        file_.close()

        for line in content.split('\n'):
            words = line.split()
            words = [word.strip().lower() for word in words]
            if not words:
                continue

            first_word = words[0]
            if first_word == 'author':
                author_name = words[1].title()
                authors.add(author_name)

    return authors


def count_values(a_dict):
    values = set()
    for value in a_dict.values():
        values.add(value)
    return len(values)


def add_sparse_vectors(vec_1, vec_2):

    # creating a new vec means this function is side-effect free
    result = {}

    for key, val in vec_1.items():
        if key in vec_2:
            result[key] = val + vec_2.pop(key)
        else:
            result[key] = val

    for key, val in vec_2.items():
        result[key] = val

    return result


def sparse_vector_product(vec_1, vec_2):

    temp = {}

    for key, val in vec_1.items():
        if key in vec_2:
            # if key not in vec_2 it is 0
            temp[key] = val * vec_2.pop(key)

    return sum(temp.values())


class TestFindDups(unittest.TestCase):

    def test_empty(self):
        got = find_dups([])
        assert got == set()

    def test_one_member(self):
        got = find_dups([1])
        assert got == set()

    def test_two_no_duplicates(self):
        got = find_dups([1, 2])
        assert got == set([])

    def test_two_duplicates_of_ones(self):
        got = find_dups([1, 1])
        assert got == set([1])

    def test_two_duplicates_of_fours(self):
        got = find_dups([1, 4, 4, 3])
        assert got == set([4])

    def test_no_duplicates(self):
        got = find_dups(range(10))
        assert got == set([])

    def test_no_duplicates(self):
        five_to_ten = range(4, 10)
        one_to_a_hundred = range(100)
        one_to_a_hundred.extend(five_to_ten)
        got = find_dups(one_to_a_hundred)
        assert got == set(five_to_ten)


class TestMatingPairs(unittest.TestCase):

    def test_example(self):

        males = range(5)
        females = 'abcdefg'[:5]

        got = mating_pairs(males, females)

        for pair in got:
            male, female = pair[0], pair[1]
            assert male in males
            assert female in females


class TestPDBFileAuthorParser(unittest.TestCase):

    def test_no_author_file(self):

        no_author_file = StringIO(
            '\n\nStuff in a PDB file'
        )

        authors = get_authors([no_author_file])
        assert authors == set()

    def test_one_author_file(self):
        one_author_file = StringIO(
            'AUthoR\tGreg\n'
            'Other stuff'
        )
        authors = get_authors([one_author_file])
        assert authors == set(['Greg'])

    def test_two_author_file(self):
        two_author_file = StringIO(
            'AUTHOR Naomi\n'
            'AUTHOR Greg\n'
        )
        authors = get_authors([two_author_file])
        assert authors == set(['Naomi', 'Greg'])

    def test_multiple_files_and_name_capitalised(self):
        no_author_file = StringIO(
            '\n\nStuff in a PDB file'
        )

        one_author_file = StringIO(
            'AUthoR\tangela\n'
            'Other stuff'
        )

        two_author_file = StringIO(
            'AUTHOR naomi\n'
            'AUTHOR greg\n'
        )

        authors = get_authors(
            [no_author_file, one_author_file, two_author_file]
        )
        assert authors == set(['Naomi', 'Greg', 'Angela'])


class TestCountValues(unittest.TestCase):

    def test_empty_dict(self):

        got = count_values({})
        assert got == 0

    def test_one_key_dict(self):

        got = count_values({'a': 1})
        assert got == 1

    def test_two_key_dict(self):

        got = count_values({'a': 1, 'b': 1})
        assert got == 1

    def test_three_key_dict(self):

        got = count_values({'a': 1, 'b': 1, 'c': 'awef'})
        assert got == 2

    def test_four_key_dict(self):

        got = count_values({'a': 1, 'b': 1, 'c': 'awef', 'd': 'awef'})
        assert got == 2


class TestSparseVector(unittest.TestCase):

    def test_add_empty_left_operand(self):

        vec_1 = {}
        vec_2 = {0: 4, 1: 5, 2: 6}

        got = add_sparse_vectors(vec_1, vec_2)

        assert got == vec_2

    def test_add_empty_right_operand(self):

        vec_1 = {0: 1, 1: 2, 2: 3}
        vec_2 = {}

        got = add_sparse_vectors(vec_1, vec_2)

        assert got == vec_1

    def test_add_operands_with_same_keys(self):

        vec_1 = {0: 1, 1: 2, 2: 3}
        vec_2 = {0: 4, 1: 5, 2: 6}

        got = add_sparse_vectors(vec_1, vec_2)

        assert got == {0: 5, 1: 7, 2: 9}

    def test_add_operands_with_some_different_keys(self):

        vec_1 = {0: 1, 1: 2, 2: 3}
        vec_2 = {5: 4, 1: 5, 8: 6}

        got = add_sparse_vectors(vec_1, vec_2)

        assert got == {0: 1, 1: 7, 2: 3, 5: 4, 8: 6}

    def test_product_empty_left_operand(self):

        vec_1 = {}
        vec_2 = {0: 4, 1: 5, 2: 6}

        got = sparse_vector_product(vec_1, vec_2)

        assert got == 0

    def test_product_empty_right_operand(self):

        vec_1 = {0: 1, 1: 2, 2: 3}
        vec_2 = {}

        got = sparse_vector_product(vec_1, vec_2)

        assert got == 0

    def test_product_operands_with_same_keys(self):

        vec_1 = {0: 1, 1: 2, 2: 3}
        vec_2 = {0: 4, 1: 5, 2: 6}

        got = sparse_vector_product(vec_1, vec_2)

        assert got == 32

    def test_product_operands_with_some_different_keys(self):

        vec_1 = {0: 1, 1: 2, 2: 3}
        vec_2 = {5: 4, 1: 5, 8: 6}

        got = sparse_vector_product(vec_1, vec_2)

        assert got == 10
