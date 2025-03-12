# %load test_permutation_solution.py
import unittest

class Permutations(object):

    def is_permutation(self, str1, str2):
        # TODO: Implement me
        if str1 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        if sorted(str1)==sorted(str2):
            return True
        return False


class TestPermutation(unittest.TestCase):

    def test_permutation(self, func):
        self.assertEqual(func(None, 'foo'), False)
        self.assertEqual(func('', 'foo'), False)
        self.assertEqual(func('Nib', 'bin'), False)
        self.assertEqual(func('act', 'cat'), True)
        self.assertEqual(func('a ct', 'ca t'), True)
        self.assertEqual(func('dog', 'doggo'), False)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)
    try:
        permutations_alt = PermutationsAlt()
        test.test_permutation(permutations_alt.is_permutation)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()