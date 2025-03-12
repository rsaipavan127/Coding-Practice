# %load test_rotation.py
import unittest
def is_substring( s1, s2):
        # TODO: Implement me
        if s1 is None or s2 is None:
            return False
        if len(s1)==len(s2) :
            if s2 in s1+s1:
                return True
        return False  

class Rotation(object):

        

    def is_rotation(self, s1, s2):
        # TODO: Implement me
        if is_substring(s1,s2):
            return True
        else:
            return False
        


class TestRotation(unittest.TestCase):

    def test_rotation(self):
        rotation = Rotation()
        self.assertEqual(rotation.is_rotation('o', 'oo'), False)
        self.assertEqual(rotation.is_rotation(None, 'foo'), False)
        self.assertEqual(rotation.is_rotation('', 'foo'), False)
        self.assertEqual(rotation.is_rotation('', ''), True)
        self.assertEqual(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()