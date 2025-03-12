# %load test_reverse_string.py
import unittest
class ReverseString(object):

    def reverse(self, chars):
        # TODO: Implement me
        if chars is None:
            return None
        if chars==['']:
            return ['']
        i=0
        j=len(chars)-1
        while i<j:
            chars[i],chars[j]=chars[j],chars[i]
            i+=1
            j-=1
        return chars   

class TestReverse(unittest.TestCase):

    def test_reverse(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(['']), [''])
        self.assertEqual(func(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')

    def test_reverse_inplace(self, func):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        func(target_list)
        self.assertEqual(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


def main():
    test = TestReverse()
    reverse_string = ReverseString()
    test.test_reverse(reverse_string.reverse)
    test.test_reverse_inplace(reverse_string.reverse)


if __name__ == '__main__':
    main()