# %load test_unique_chars.py
import unittest

class UniqueChars(object):

    def has_unique_chars(self, string):
        # TODO: Implement me
        li=[]
        if string is None:
            return False
        for i in string:
            if i not in li:
                li.append(i)
            else:
                return False
        return True
                
        


class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self, func):
        self.assertEqual(func(None), False)
        self.assertEqual(func(''), True)
        self.assertEqual(func('foo'), False)
        self.assertEqual(func('bar'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)
    try:
        unique_chars_set = UniqueCharsSet()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
        unique_chars_in_place = UniqueCharsInPlace()
        test.test_unique_chars(unique_chars_in_place.has_unique_chars)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()