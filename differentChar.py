# %load test_str_diff.py
import unittest

class Solution(object):

    def find_diff(self, str1, str2):
        # TODO: Implement me
        if str1 is None or str2 is None:
            return None
        s1=sorted(str1)
        s2=sorted(str2)
        for i in range(min(len(s1),len(s2))):
            if s1[i]==s2[i]:
                continue
            else:
                if len(s1)>len(s2):
                    return s1[i]
                else: 
                    return s2[i]
        return s1[-1] if len(s1)>len(s2) else s2[-1]       
    
    def find_diff_xor(self, str1, str2):
        # TODO: Implement me
        s=str1+str2
        a=0
        for i in s:
            a=a^ord(i)
        return chr(a)    
            


        


class TestFindDiff(unittest.TestCase):

    def test_find_diff(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_diff, None)
        self.assertEqual(solution.find_diff('ab', 'aab'), 'a')
        self.assertEqual(solution.find_diff('aab', 'ab'), 'a')
        self.assertEqual(solution.find_diff('abcd', 'abcde'), 'e')
        self.assertEqual(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        self.assertEqual(solution.find_diff_xor('ab', 'aab'), 'a')
        self.assertEqual(solution.find_diff_xor('aab', 'ab'), 'a')
        self.assertEqual(solution.find_diff_xor('abcd', 'abcde'), 'e')
        self.assertEqual(solution.find_diff_xor('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()