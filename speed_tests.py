import timeit
from math import log

def get_num_digits(n):
    return int(log(n, 10) + 1)

def get_num_digits2(n):
    return len(str(n))

def get_digit(n, digit):
    n = str(n)
    index = len(n) - (digit + 1)
    return int(n[index])

def get_digit2(n, digit):
    num_digits = get_num_digits2(n)
    

def test_get_num_digits():
    print(timeit.timeit('get_num_digits(37323242342323232)', setup='from __main__ import get_num_digits'))     
    print(timeit.timeit('get_num_digits2(373232423423233323)', setup='from __main__ import get_num_digits2'))
    
def test_get_digit():
    print(timeit.timeit('get_digit(37323242342323232, 4)', setup='from __main__ import get_digit'))     
    print(timeit.timeit('get_digit2(37323242342323232, 4)', setup='from __main__ import get_digit2'))
    
if __name__ == '__main__':
    """ Test stuff. """
    test_get_digit()
        
    