#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Solutions to problems on Project Euler (www.projecteuler.net) Problems 21-40
"""
from math import *

SHELVED_FILE = "numbers_and_factors"

def calc_primes_less_than_n(nmax):
    """
    Calculates all primes < nmax
    """
    #  Because the algorithm used doesn't work for the number 2, it needs to be initialized.
    primes_found = set([2])
    
    current_number = 3
    while current_number < nmax:
        number_is_prime = True
        
        for prime_number in primes_found:
            # This loop divides current_number by every prime number found so far that is less than the checking_limit.
            # checking_limit is the sqrt of checkingNumber, because it is an efficient way to do it.
        
            checking_limit = sqrt(current_number) # No need to check numbers higher than the square root.
            if prime_number <= checking_limit:
                if current_number % prime_number == 0:
                    number_is_prime = False
                    break
            else:
                break
            
        if number_is_prime:
            primes_found.add(current_number)
            
        current_number += 1    
    return primes_found

def shelve_primes_less_than_n(n=10000000):
    import shelve
    primes_less_than_n = calc_primes_less_than_n(n)
    myfile = shelve.open('primes_less_than' + str(n))
    myfile['primes_less_than' + str(n)] = primes_less_than_n
    myfile.close()
    print('Consider it shelved.')


def shelve_numbers_factors(max_num=50000):
    """Stores numbers and the sums of their factors up to 28123 for later use"""
    import shelve
    myfile = shelve.open('numbers_and_factors')
    numbers_factors = get_numbers_and_summed_factors(max_num)
    myfile['numbers_factors'] = numbers_factors
    myfile.close()

def uniquify_list(list_):
    pass


def prob21(max_num):
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide 
    evenly into n). If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair 
    and each of a and b are called amicable numbers.
    
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
    
    Evaluate the sum of all the amicable numbers under 10000.
    """
    
    # numbers_factors is a list of tuples of the form (number, prime_factors)
    numbers_factors = get_numbers_and_summed_factors(max_num)
    
    # Each pair is listed twice in the amicable_pairs list
    amicable_pairs = get_amicable_pairs(max_num, numbers_factors)

    unique_numbers = []
    
    for pair in amicable_pairs:
        unique_numbers.append(pair[0])
    
    sum_of_amicable_pairs = sum(unique_numbers)
    print("The sum of amicable pairs <= %s is %s" % (max_num, sum_of_amicable_pairs))
    
def get_amicable_pairs(max_num, numbers_factors):
    amicable_pairs = []
    
    for number_factor in numbers_factors:
        current_num = number_factor[0]
        current_sum = number_factor[1]
        
        if current_sum <= max_num:
            number_matches_sum = (current_num == numbers_factors[current_sum - 2][1])
            perfect_number = current_num == current_sum
            
            is_amicable =  number_matches_sum and not perfect_number
            
            if is_amicable:
                amicable_pairs.append((current_num, current_sum))
    return amicable_pairs

def get_numbers_and_summed_factors(max_num):
    '''Returns a list of tuples of number/combo pairs'''
    numbers_factors = [] # used to store (number, factor) tuples
    primes_found = []
    num = 2
    while num <= max_num:

        prime_factors_of_num = get_prime_factors(num, primes_found)
        all_num_factors = get_all_factors(num, prime_factors_of_num)
        sum_of_factors = sum(all_num_factors)
        numbers_factors.append((num,sum_of_factors))
        
        num += 1
    return numbers_factors
        
def get_prime_factors(n, primes_found):
    '''
    Given a list of prime numbers < n, return all of n's prime factors
    '''
    factors = [1]
    test_limit = sqrt(n)
    for prime in primes_found:
        if prime > test_limit:
            break
            while n % prime == 0:
                factors.append(prime)
                n /= prime
            
    if n != 1 and n not in primes_found:
        primes_found.append(n)
        
    return factors
            
def get_all_factors(n, prime_factors):
    """Gives a list of all """
    all_factors = []
    for prime in prime_factors:
        if prime not in all_factors:
            all_factors.append(prime) 
    
    for prime in prime_factors:
        for factor in all_factors:
            test_factor = prime * factor
            if (n % test_factor == 0) and (test_factor not in all_factors) and (test_factor != n):
                all_factors.append(test_factor)

    return all_factors
            

def prob22():
    """
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
    containing over five-thousand first names, begin by sorting it into 
    alphabetical order. Then working out the alphabetical value for each name, 
    multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 
    3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a 
    score of 938 * 53 = 49714.
    
    What is the total of all the name scores in the file?
    """
    import csv
    
    alpha_dict = get_alphabet_dict()
    with open("names.txt", newline='') as csvfile:
        namesfile = csv.reader(csvfile, delimiter = ',', quotechar='"')
    
        for row in namesfile:
            names = row
    names.sort()
    
    total_value = 0
    for index, name in enumerate(names):
        name_value = 0
        multiplier = index + 1
        for letter in name:
            name_value += alpha_dict[letter]
        
        name_value *= multiplier
        total_value += name_value
    
    print('The sum of all the name values in the list of names is %s' % total_value)

def get_alphabet_dict():
    alpha_dict = {}
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for index, letter in enumerate(alphabet):
        alpha_dict[letter] = index + 1 # add 1 to get 1 - 26 instead of 0 - 25
    
    return alpha_dict


def prob23(max_num=20162):
    """
    A perfect number is a number for which the sum of its proper divisors is exactly 
    equal to the number. For example, the sum of the proper divisors of 28 would be 
    1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n 
    and it is called abundant if this sum exceeds n.
    
    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
    that can be written as the sum of two abundant numbers is 24. By mathematical 
    analysis, it can be shown that all integers greater than 28123 can be written as 
    the sum of two abundant numbers. However, this upper limit cannot be reduced any 
    further by analysis even though it is known that the greatest number that cannot 
    be expressed as the sum of two abundant numbers is less than this limit.
    
    Find the sum of all the positive integers which cannot be written 
    as the sum of two abundant numbers.
    """
    
    # All the numbers and their factors up to 28123 have been stored
    # using shelve in the file 'primes_and_factors'
    import shelve
    primes_file = shelve.open('numbers_and_factors')
    numbers_factors = primes_file['numbers_factors'][0:max_num - 1] # Subtract 1 because the list's 0th element is (2,1)
    primes_file.close()
    
    abundant_numbers = get_abundant_numbers(numbers_factors)
    
    unique_sums = get_unique_sums(max_num, abundant_numbers)
    not_a_sum = [number for number in range(1, max_num+1) if number not in unique_sums]
    prob23_answer = sum(not_a_sum)
    print('The sum of all numbers that can\'t be expressed as the sum of two abundant numbers is %s\n' % prob23_answer)
    
    
def get_unique_sums(max_num, abundant_numbers):
    """
    Given a list of numbers, scrolls through the list to give all pairs of 
    unique sums.
    """
    unique_sums = set()
    numbers_list_length = len(abundant_numbers)
    
    # get every unique sum by scrolling through the list of 
    # abundant numbers and adding each number to every other
    # number in the list.
    for num1 in abundant_numbers:
        
        # add number to every other element in the list
        # of abundant numbers
        for num2 in abundant_numbers:
            
            unique_sums.add(num1 + num2)
                
    return unique_sums

def get_abundant_numbers(numbers_factors):
    """
    Given a list of tuples of the form (number, sum_of_factors), return a list
    of abundant numbers
    
    An abundant number is defined as a number which has a greater sum of factors than itself.
    """
    sum = 1 # index for num_fact
    num = 0 # index for num_fact
    
    abundant_numbers = set()
    
    for num_fact in numbers_factors:
    
        if num_fact[sum] > num_fact[num]:
        
            abundant_numbers.add(num_fact[num])
    
    return abundant_numbers


def prob24(string_to_sort, nth_permutation):
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
    permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed 
    numerically or alphabetically, we call it lexicographic order. The lexicographic 
    permutations of 0, 1 and 2 are:

    012   021   102   120   201   210
    
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    
    ordered_list = sort_string_nth_permutation(string_to_sort, nth_permutation)
    ordered_string = ''
    for char in ordered_list:
        ordered_string += char
    print("Permutation # %d of %s is %s" % (nth_permutation, string_to_sort, ordered_string))
    
def sort_string_nth_permutation(string_to_sort, nth_permutation, permutation_count=0, ordered_list=[]):
    """
    Given a string in some order, this returns a string of the nth permutation.
    
    First, it turns string_to_sort into a list of characters, because that is easier
    to work with.  It finds what the first character will be, then takes that
    character out of the list and appends it to ordered_list.  The rest of the
    original list goes back through this function.
    """
    
    if type(string_to_sort) == str:
        place_holder_list = []

        for character in string_to_sort:
            place_holder_list.append(character)

        string_to_sort = place_holder_list
    
    # the number of times through this while loop determines how many
    # places to the right to look for the digit that belongs in the
    # first digit's place.
    
    places_to_right = 0
    
    while len(string_to_sort) > 0:
        
        next_permutation = permutation_count + factorial(len(string_to_sort) - 1)
        
        if next_permutation < nth_permutation:
            permutation_count = next_permutation
            places_to_right += 1
        
        elif next_permutation == nth_permutation:
            ordered_list.append(string_to_sort.pop(places_to_right))
            places_to_right = 0
       
        else:
            ordered_list.append(string_to_sort.pop(places_to_right))
            places_to_right = 0 
    
    # ordered_list.append(string_to_sort.pop())
    
    return ordered_list

def prob25(max_num):
    """
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

    The 12th term, F12, is the first term to contain three digits.    
    What is the first term in the Fibonacci sequence to contain 1000 digits?
    """
    counter = fibonacci_until(max_num)
    print('Term %s is the first term in the Fibonacci sequence greater than %s' %(counter, max_num))

def fibonacci_until(max_num):
    """Does a fibonacci sequence until the term is greater than max_num"""
    a = 1
    b = 1
    term_counter = 2
    while b <= max_num:
        b += a
        a = b - a        
        term_counter += 1
    
    
    return term_counter


def prob26(max_num):
    """
    A unit fraction contains 1 in the numerator. The decimal representation 
    of the unit fractions with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It 
    can be seen that 1/7 has a 6-digit recurring cycle.
    
    Find the value of d 1000 for which 1/d contains the longest recurring 
    cycle in its decimal fraction part.
    """
    
    max_repetitions = 0
    answer = 0 
    for number in range(1, max_num + 1):
        repeating_digits_num = get_repeating_digits(number)
        if repeating_digits_num > max_repetitions:
            max_repetitions = repeating_digits_num
            answer = number
    
    print('The best number is %s, it repeats %s digits' % (answer, max_repetitions))
    
def get_repeating_digits(number):
    """
    Gets the number of repeating decimals in 1 / number
    """
    next_remainder = 'foo' # need to initialize this
    remainders = []
    digits = [] # this is unnecessary, and just for fun.
    divisor = number
    dividend = 10 # skips the first, unnecessary step of checking if divisor > dividend
    started_repeating = False
    
    while not started_repeating:
        if divisor > dividend:
            dividend *= 10
      
        elif dividend % divisor == 0:
            remainders = []
            break
        
        else:
            next_digit = int(dividend / divisor)
            next_remainder = dividend % divisor
            
            if next_remainder in remainders:
                started_repeating = True
                
            else:
                digits.append(next_digit)
                remainders.append(next_remainder)
                dividend = next_remainder * 10
            
    
    if len(remainders) == 0:
        answer =  0
        
    else:
        answer = len(remainders) - remainders.index(next_remainder)

    return answer


def prob27(min_num=-1000, max_num=1000):
    """
    Euler published the remarkable quadratic formula:

    n**2 + n + 41
    
    It turns out that the formula will produce 40 primes for the 
    consecutive values n = 0 to 39. However, when 
    n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and 
    certainly when n = 41, 41� + 41 + 41 is clearly divisible by 41.
    
    Using computers, the incredible formula  n�  79n + 1601 was 
    discovered, which produces 80 primes for the consecutive 
    values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.
    
    Considering quadratics of the form:
    n**2 + an + b, where |a|  1000 and |b|  1000
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |4| = 4
    
    Find the product of the coefficients, a and b, for the quadratic 
    expression that produces the maximum number of primes for 
    consecutive values of n, starting with n = 0.
    """
    import shelve
    
    primes_file = shelve.open(SHELVED_FILE)
    primes = primes_file["list_of_primes"][0:1000]
    primes_file.close()
    a = b = min_num + 1
    best_a = 0
    best_b = 0
    max_consecutive_primes = 0
    
#    while a < max_num:
#        while b < max_num:
    for a in range(min_num + 1, max_num):
        for b in range(min_num + 1, max_num):
            if (b <= 1) or (a % 2 == 0):
                still_looking = False
            else:
                still_looking = True
            n = 0
            consecutive_primes = 0
            
            while still_looking:
            
                test_prime = n ** 2 + a * n + b
            
                if test_prime in primes:
                    consecutive_primes += 1
                    n += 1
                
                else:
                    still_looking = False
                    
                    
            if consecutive_primes > max_consecutive_primes: 
                max_consecutive_primes = consecutive_primes
                best_a = a
                best_b = b
            
#            b+=1
        
#        a+=1
    
    answer = best_a * best_b
    
    print('The a and b that produce the most primes are %d and %d.  Their product is %d' %(best_a, best_b, answer))
    
        
def prob28(dimension):
    """
    Starting with the number 1 and moving to the right in a 
    clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    
    It can be verified that the sum of the numbers on the diagonals is 101.
    
    What is the sum of the numbers on the diagonals in a 
    1001 by 1001 spiral formed in the same way?
    """
    sum_ = 0
    
    original_dimension = dimension
    
    while dimension > 1:
        dimension_squared = dimension * dimension
        increment = dimension - 1
        
        top_right = dimension_squared
        top_left = top_right - increment
        bottom_left = top_left - increment
        bottom_right = bottom_left - increment
        sum_ += top_right + top_left + bottom_left + bottom_right
        
        dimension -= 2
    
    sum_ += 1
    
    print("The sum of a %dx%d square is %d" % (original_dimension, original_dimension, sum_))
    
def prob29(amax, bmax):
    """
    Consider all integer combinations of ab for 2 < a < 5 and 2 < b < 5:

    2**2=4,  2**3=8,   2**4=16,  2**5=32
    3**2=9,  3**3=27,  3**4=81,  3**5=243
    4**2=16, 4**3=64,  4**4=256, 4**5=1024
    5**2=25, 5**3=125, 5**4=625, 5**5=3125
    
    If they are then placed in numerical order, with any repeats removed, 
    we get the following sequence of 15 distinct terms:
    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
    How many distinct terms are in the sequence generated by a**b for 2 < a < 100 and 2 < b < 100?
    """
    
    distinct_terms = set()
    
    for a in range(2, amax + 1):
        for b in range(2, bmax + 1):
            distinct_terms.add(a ** b)
    
    num_terms = len(distinct_terms)
    
    print("There are %d distinct terms for all combinations of a**b from 2 to %d" %(num_terms, amax))
    
    
def prob30(power):
    """
    Find all numbers that can be written as the sum of 
    each digit to the 5th.
    """
    max_sum = get_max_sum(power)
    best_numbers = [] # contains a list of all numbers that fit the criteria above
    
    for number in range(2, max_sum):
        sum_of_digits_to_power = get_sum_of_digits_to_power(number, power)
    
        if number == sum_of_digits_to_power:
            best_numbers.append(number)
    
    answer = sum(best_numbers)
    print('The sum of all numbers that can be written as each digit to the power of %d is %d ' % (power, answer))

def get_sum_of_digits_to_power(number, power):
    sum_of_digits_to_power = 0
    for digit in str(number):
        sum_of_digits_to_power += int(digit) ** power
        
    return sum_of_digits_to_power
    
def get_max_sum(power):
    """
    returns the max number you need to check to in order to find all
    numbers which can be expressed as the sum of their digits to power.
    """ 
    max_sum = 9 ** power
    num_digits = 1
    
    while len(str(max_sum)) >= num_digits:
        max_sum = num_digits * 9 ** power
        num_digits += 1
        
    
    return max_sum


def prob31():
    '''
    In England the currency is made up of pound, £, and pence, 
    p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:
    
    1£1 + 150p + 220p + 15p + 12p + 31p
    How many different ways can £2 be made using any number of coins?In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
    
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:
    
    1 * £1 + 1 * 50p + 2 *20p + 1 * 5p + 1 * 2p + 3 * 1p
    How many different ways can £2 be made using any number of coins?
    '''
    
    P2 = 2
    P5 = 5
    P10 = 10
    P20 = 20
    P50 = 50
    P100 = 100
    P200 = 200
    
    times_in_loop = 0
    num_ways = 0
    for p200 in range(200 // P200 + 1):
     for p100 in range(200 // P100 + 1):
      for p50 in range(200 // P50 + 1):
       for p20 in range(200 // P20 + 1):
        for p10 in range(200 // P10 + 1):
         for p5 in range(200 // P5 + 1):
          for p2 in range(200 // P2 + 1):
            times_in_loop += 1
            coin_sum = p200*P200 + p100*P100 + p50*P50 + p20*P20 + p10*P10 + p5*P5 + p2*P2 
            if coin_sum <= 200:
                num_ways += 1
            else:
                break
    
    print('The number of ways to make 2 pounds is %d' % num_ways)
    print('The number of times through the loop is %d' % times_in_loop)


def get_coin_total(coins, target, so_far, coin):
    global numcalls
    numcalls += 1
    
    if coin == 0: 
        amount_needed = so_far - target
        if amount_needed % coins[0] == 0 and amount_needed <= target: return 1
        else: return 0
    
    if so_far == target: return 1
    elif so_far > target: return 0
    
    total = 0
    for my_coin in range(coin, -1, -1):
        total += get_coin_total(coins, target, so_far + coins[my_coin], my_coin)
    
    return total

def prob31_backtrack(coins, to_make):
    '''
    Problem 31, implementing backtracking.
    
    @param coins the list of coin denominations
    @param to_make, the amount desired
    @param so_far, the amount of money I've made so far
    @param num_combinations, the number of combinations found so far.
    '''

    coins.sort()
    total_combinations = get_coin_total(coins, to_make, 0, len(coins) - 1)
    print('The function  was called {0} times'.format(numcalls))
    print(total_combinations)


def test_prob31():
    # coins = [200, 2, 5, 10, 20, 50, 100, 1]
    # to_make = 200
    
    coins = [2,3,4]
    to_make = 12
    prob31_backtrack(coins, to_make)
        
    
def prob32():
    '''
    We shall say that an n-digit number is pandigital if it makes use 
    of all the digits 1 to n exactly once; for example, the 5-digit 
    number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 * 186 = 7254, 
    containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product 
    identity can be written as a 1 through 9 pandigital.
    
    HINT: Some products can be obtained in more than one way so be 
    sure to only include it once in your sum.
    '''
    pass


def prob33():
    '''
    The fraction 49/98 is a curious fraction, as an inexperienced 
    mathematician in attempting to simplify it may incorrectly 
    believe that 49/98 = 4/8, which is correct, is obtained by 
    cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, 
    less than one in value, and containing two digits in the numerator 
    and denominator.

    If the product of these four fractions is given in its lowest 
    common terms, find the value of the denominator.
    '''
    
    curious_fractions = []
    for denominator in range(11,100):
        for numerator in range(10,denominator):
            
            new_fraction = check_digits(denominator, numerator)
            
            if new_fraction is not None:
                new_num = new_fraction[0]
                new_denom = new_fraction[1]
                
                try:
                    if new_num / new_denom == numerator / denominator:
                        curious_fractions.append((numerator, denominator))
                    
                except ZeroDivisionError:
                    print(numerator, denominator)
    print('curious fractions: {0}'.format(curious_fractions))
    
    num_product = 1
    den_product = 1
    for curious_fraction in curious_fractions:
        num_product *= curious_fraction[0]
        den_product *= curious_fraction[1]
        
    print('new numerator: {0}   new denominator: {1}'.format(num_product, den_product))
    

def check_digits(denom, num):
    '''
    Checks to see if the denominator and numerator have the same digit
    The digit cannot be zero.
    '''
    if denom == num:
        return None
    
    denom = str(denom)
    num = str(num)
    
    for den_position, character in enumerate(denom):
        if character != '0' and character in num:
            num_position = num.find(character)
            
            if den_position == 0:
                new_denom = int(denom[1])
            else:
                new_denom = int(denom[0])
                
            if num_position == 0:
                new_num = int(num[1])
            
            else:
                new_num = int(num[0])
            
            return (new_num, new_denom)
    else:
        return None
    

            
            
            
def prob34(max_num = 1854721):
    '''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the 
    factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    '''
    factorions = []
    for num in range(10, max_num):
        sum_factorials = sum(factorial(int(i)) for i in str(num))
        if num == sum_factorials:
            factorions.append(num)
    print('The factorions are {0}\nTheir sum is {1}'.format(
           factorions, sum(factorions)))

def prob35():
    '''
    The number, 197, is called a circular prime because all 
    rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 
    100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    
    How many circular primes are there below one million?
    '''
    
def prob36():
    '''
    The decimal number, 585 = 1001001001 (binary), is palindromic 
    in both bases.

    Find the sum of all numbers, less than one million, which are 
    palindromic in base 10 and base 2.
    
    (Please note that the palindromic number, in either base, 
    may not include leading zeros.)
    '''
    
    
def prob37():
    '''
    The number 3797 has an interesting property. Being prime itself, 
    it is possible to continuously remove digits from left to right, 
    and remain prime at each stage: 3797, 797, 97, and 7. 
    Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable 
    from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    '''
    
def prob38():
    '''
    Take the number 192 and multiply it by each of 1, 2, and 3:
    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 
    192384576. We will call 192384576 the concatenated product 
    of 192 and (1,2,3)
    
    The same can be achieved by starting with 9 and multiplying 
    by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is 
    the concatenated product of 9 and (1,2,3,4,5).
    
    What is the largest 1 to 9 pandigital 9-digit number that can be 
    formed as the concatenated product of an integer with 
    (1,2, ... , n) where n = 1?
    '''
    

def prob39():
    '''
    If p is the perimeter of a right angle triangle with integral 
    length sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p < 1000, is the number of solutions maximised?
    '''

def prob40():
    '''
    An irrational decimal fraction is created by concatenating 
    the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.
    
    If dn represents the nth digit of the fractional part, find the 
    value of the following expression.
    
    d1  d10  d100  d1000  d10000  d100000  d1000000
    '''

if __name__ == "__main__":
#    prob21(10000)
#    prob22()
#    prob23(20162)
#    prob24('0123456789', 1000000)
#    prob25(10**999)
#    prob26(2000)
#    prob27(-1000, 1000) # takes about 12 s to run
#    prob28(1001)
#    prob29(100, 100)
#    prob30()
#    prob31()
#    prob33()
#    prob34()

#    test_prob31()
    shelve_primes_less_than_n(1000000)
    pass