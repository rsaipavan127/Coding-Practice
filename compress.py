# %load test_compress.py
import unittest

class CompressString(object):

    def compress(self, string):
        # TODO: Implement me
        count=1
        compress=[]

        if string is None:
            return None
        if string == '':
            return ''
        for i in range(1,len(string)):
            if string[i]==string[i-1]:
                count+=1
            else:
                compress.append(string[i-1])
                if count > 1:
                    compress.append(str(count))
                count =1    
        compress.append(string[-1])
        if count>1:
                compress.append(str(count))  
        res=''.join(compress) 
        if len(res) < len(string):
            return res   

        else : return string
       


class TestCompress(unittest.TestCase):

    def test_compress(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDDE'), 'A3BC2D4E')
        self.assertEqual(func('BAAACCDDDD'), 'BA3C2D4')
        self.assertEqual(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    compress_string = CompressString()
    test.test_compress(compress_string.compress)


if __name__ == '__main__':
    main()