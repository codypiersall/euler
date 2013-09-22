import timeit
from math import log

def get_num_digits(n):
    return int(log(n, 10) + 1)

def get_num_digits2(n):
    return len(str(n))

if __name__ == '__main__':
    # print(timeit.timeit('get_num_digits(37323242342323232)', setup='from __main__ import get_num_digits'))     
    # print(timeit.timeit('get_num_digits2(373232423423233323)', setup='from __main__ import get_num_digits2')) 