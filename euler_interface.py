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

def doprob3():
    number = 600851475143
    answer = s.prob3(number)
    
    answer_text = 'The largest prime factor of {} is {}'
    print(answer_text.format(number, answer))
    
def doprob4():
    number_digits = 3
    answer = s.prob4(number_digits)
    
    answer_text = 'The largest palindrome made from the product of two {}-digit numbers is {}'
    print(answer_text.format(number_digits, answer))
    
def doprob5():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = 'The smallest number that is divisible by each number from 1 to {} is {}'
    print(answer_text.format(maxnum, answer))

def doprob6():
    number = 100
    answer = s.prob6(number)
    
    answer_text = 'The difference between the sum of the squares and square of the sum of the first {} numbers is {}'
    print(answer_text.format(number, answer))

def doprob7():
    nth_prime_to_find = 10001
    answer = s.prob7(nth_prime_to_find)
    
    answer_text = 'The {}th prime is {}'
    print(answer_text.format(nth_prime_to_find, answer))

def doprob8():
    number_as_string ='7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450' 
    num_length = len(number_as_string)
    answer = s.prob8(number_as_string)
    
    answer_text = 'The greatest product in the {} digit number is {}'
    print(answer_text.format(num_length, answer))

def doprob9():
    number = 1000
    answer = s.prob9(number)
    
    answer_text = 'The product of a triangle with the perimeter {} is {}'
    print(answer_text.format(number, answer))

def doprob10():
    maxnum = 1000000
    answer = s.prob10(maxnum)
    
    answer_text = 'The sum of the primes less than {} is {}'
    print(answer_text.format(maxnum, answer))

def doprob11():
    answer = s.prob11()
    
    answer_text = 'The largest product in the 20 x 20 grid is {}'
    print(answer_text.format(answer))

def doprob12():
    num_divisors = 500
    answer = s.prob12(num_divisors)
    
    answer_text = 'The first triangular number with {} divisors is {}'
    print(answer_text.format(num_divisors, answer))

def doprob13():
    answer = s.prob13()
    
    answer_text = 'The first ten digits of the sum of the one-hundred 50-digit numbers is {}'
    print(answer_text.format(answer))

def doprob14():
    maxnum = 1000000
    answer = s.prob14(maxnum)
    
    answer_text = 'The starting number below {} with the most terms in the Collatz sequence is {}'
    print(answer_text.format(maxnum, answer))

def doprob15():
    rows = columns = 20
    answer = s.prob15(rows, columns)
    
    answer_text = 'There are {} unique ways to get from one corner to its opposite on a {}x{} grid.'
    print(answer_text.format(answer, rows, columns))

def doprob16():
    base = 2
    exp = 100
    answer = s.prob16(base, exp)
    
    answer_text = 'The sum of the digits of {}**{} is {}'
    print(answer_text.format(base, exp, answer))

def doprob17():
    minnum = 1
    maxnum = 1000
    answer = s.prob17(minnum, maxnum)
    
    answer_text = 'Writing out all numbers from {} to {} takes {} letters'
    print(answer_text.format(minnum, maxnum, answer))

def doprob18():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob19():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob20():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob21():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob22():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob23():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob24():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob25():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob26():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob27():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob28():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob29():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob30():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob31():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob32():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob33():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob34():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob35():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob36():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob37():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob38():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob39():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob40():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob41():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob42():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob43():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob44():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob45():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob46():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob47():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob48():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob49():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))

def doprob50():
    maxnum = 20
    answer = s.prob5(maxnum)
    
    answer_text = ''
    print(answer_text.format(maxnum, answer))


if __name__ == '__main__':
    
    doprob17()