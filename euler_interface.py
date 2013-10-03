import solutions as s

def doprob1():
    upto = 1000
    divisible_by = 3, 5
    answer = s.prob1(upto, divisible_by)
    print('The sum of all numbers less than {} divisible by {} is {}'.format(upto, divisible_by, answer))


def doprob2():
    maxnum = 1000000
    answer = s.prob2(maxnum)
    answer_text = 'The sum of all even Fibonacci numbers less than {} is {}'
    
    print(answer_text.format(maxnum, answer))

    
if __name__ == '__main__':
    
    doprob2()    