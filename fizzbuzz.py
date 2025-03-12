# %load test_fizz_buzz.py
import unittest
class Solution(object):

    def fizz_buzz(self, num):
        # TODO: Implement me
        if num is None:
            raise TypeError("is is null")
        if not num or num < 1:
            raise ValueError("it is zero or Negative")
        change=[]
        for i in range(1,num+1):
            if i%3==0 and i%5==0:
                change.append("FizzBuzz")
            elif i%3==0:
                change.append("Fizz")
            elif i%5==0:
                change.append("Buzz")
            else:
                change.append(str(i))
        return change            

                
        
        pass

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.fizz_buzz, None)
        self.assertRaises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()