"""
Solutions to problems on Project Euler
"""

__author__ = 'Cody Piersall'

import copy
import shelve
from math import sqrt, factorial, log
import numpy as np

SHELVED_FILE = "numbers_and_factors"

def generate_hexagonal_numbers(m, n):
    """Generate the mth to nth hexagonal numbers.
    A hexagonal number is a number which has an integer solution
    for Hn=n(2n−1)
    
    """
    
    return (i * (2*i - 1) for i in range(m, n+1))
    
def generate_pentagonal_numbers(m, n):
    """Generate the mth to nth pentagonal numbers.
    A pentagonal number is a number which has an integer solution
    for Pn=n(3n−1)/2
    
    """
    
    return (i * (3*i - 1)//2 for i in range(m, n+1))
    
def generate_triangular_numbers(m, n):
    """Generate the mth to nth triangular numbers.
    A triangular number is a number which has an integer solution
    for tn = ½n(n+1)
    
    """
    
    return (.5*i *(i + 1) for i in range(m, n+1))
    
def is_prime(n):
    """return True if n is prime, else False"""
    max_val = int(sqrt(n)) + 1
    for i in range(2, max_val):
        if n % i == 0:
            return False
    
    return True

def get_gcf(m, n):
    """ Return the greatest common factor of m and n.
    
    Algorithm from Structure and Interpretation of Computer Programs.
    
    """
    m, n = max([m,n]), min([m,n])
            
    def recurse(a, b):
        if b == 0:
            return a
        else:
            return recurse(b, a % b)
    
    return recurse(m, n)

def locations_of_substring(string, substring):
    """Return a list of locations of a substring."""
    
    substring_length = len(substring)    
    def recurse(found_so_far, start):
        location = string.find(substring, start)
        if location != -1:
            return recurse(found_so_far + [location], location+substring_length)
        else:
            return found_so_far

    return recurse([], 0)

def replace_digits(number):
    """
    For a number of the form 43***2* where a * represents a digit,
    yield every number that can be formed by replacing * with numbers.
    
    """
    
    num_stars = number.count('*')
    first_star = number.find('*')
    if num_stars == 1:
        for num in range(10):
            yield int(number[:first_star] + str(num) + number[first_star+1:])
    else:
        for num in range(10):
            yield from replace_digits(number[:first_star] + str(num) + number[first_star+1:])

def replace_digits_with_single_number(number_with_blanks, replace_char='*'):
    """ 
    Given a number of the for 43***2* where * represents a digit,
    yield every number that can be formed by replacing * with a single number.
    
    """
    
    for i in range(10):
        yield int(number_with_blanks.replace(replace_char, str(i)))
            
def get_lcm(m, n):
    """ Return the least common multiple of m and n """
    
    return (m // get_gcf(m, n)) * n
    
def divisible_by_any(n, numbers):
    """for i in range(1,n), return list of numbers divisible by any number in numbers """
    return [i for i in range(1,n) if any(i % a == 0 for a in numbers)]
    

def filter_list_by_divisible(fibonacci_numbers, divisor=2):
    '''
    returns a list from a list of numbers divisible by divisor.
    '''
    divisible_fib_nums = []
    for number in fibonacci_numbers:
        if number % divisor == 0:
            divisible_fib_nums.append(number)
    
    return divisible_fib_nums


def fibonacci(maxnum, less_than=True):
    """
    Calculates the numbers in the fibonacci sequence.
    If less_than==True, 
    """
    fib_nums = [1,1]
    
    while fib_nums[-1] <= maxnum:
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)
        
    # The above while loop added one number too many; time to take it off.
    if less_than: fib_nums.pop()
    return fib_nums

def numbers_are_permutations(numbers):
    """
    Check that every number in numbers is a permutation of each other
    """
    first_num = sorted(str(numbers[0]))
    for num in numbers[1:]:
        if first_num != sorted(str(num)):
            return False
    return True
    
def get_prime_factors3(n, primes):
    """ 
    Return prime factors of n from iterable of primes
    """
    
    factors = []
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n /= prime
        if n < prime:
            break
    
    return factors
    
def get_prime_factors2(n, primes_less_than_n):
    '''
    Given a list of prime numbers < n, return all of n's prime factors
    '''
    factors = []
    for prime in primes_less_than_n:
            while n % prime == 0:
                factors.append(prime)
                n /= prime
            
    if n != 1 and n not in primes_less_than_n:
        primes_less_than_n.append(n)
        
    return factors
            

def get_prime_factors(n):
    '''
    Return a list of prime factors of n
    '''
    divisors = []
    divided_number = n
    while divided_number != 1:
        divisor = 2
        
        while divisor <= divided_number:
            
            if divided_number % divisor == 0:
                divisors.append(divisor)
                divided_number = divided_number / divisor
            
            else:
                divisor += 1
    return divisors


def number_is_palindrome(n):
    n = str(n)
    return ispalindrome(n)
        

def sum_squares(n):
    """Square each number from 1 to n, and return the sum."""
    sum_of_squares = 0
    for num in range(1, n + 1):
        sum_of_squares += num ** 2
    return sum_of_squares
        
def square_sum(n):
    """sum numbers from 1 to n, and return it squared."""
    square_of_sum = sum(range(1, n + 1)) ** 2
    return square_of_sum


def calc_nth_prime(nth_prime):
    """Return the nth prime number."""
    #  Because the algorithm used doesn't work for the number 2, it needs to be initialized.
    primes_found = [2]
    num_primes_found = 1
    
    current_number = 3
    while num_primes_found < nth_prime:
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
            primes_found.append(current_number)
            num_primes_found += 1
            
        current_number += 1    
        
    return primes_found


def analyze_string(string, consecutive_digits=5):
    """Multiplies every group of 5 consecutive numbers together, stores results in a list."""
    string_length = len(string)
    iterations_needed = string_length - consecutive_digits + 1
    
    products = []
    
    for digit in range(1, iterations_needed):
        current_digits = string[digit:digit + 5]
    
        if '0' in current_digits:
            pass
        else:
            product = multiply_digits(current_digits)
            products.append(product)
    return products

def multiply_digits(string_of_digits):
    product = 1
    for digit in string_of_digits:
        digit = int(digit)
        product *= digit
    return product


def calc_primes_less_than_n(nmax):
    """
    Method calculates the nth prime number.  It stores each found prime number into
    a list, and only divides the current number being tested by the previously found
    prime numbers.
    """
    #  Because the algorithm used doesn't work for the number 2, it needs to be initialized.
    primes_found = [2]
    
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
            primes_found.append(current_number)
            
        current_number += 1    
        
    return primes_found
 
 
def get_products(number_grid):
    products = []
    num_rows = len(number_grid) # this only happens to be true because it is a square grid
    for row in range(0, num_rows):
        for col in range(0, row):
            horizontal_products(number_grid, row, col, products)
            vertical_product(number_grid, row, col, products)
            SW_product(number_grid, row, col, products)
            NE_product(number_grid, row, col, products)

    return products

def horizontal_products(number_grid, row, col, products):
    if col <= 16:
        product = 1
        for index in range(0, 4):
            colindex = col + index
            product *= number_grid[row][colindex]
            
        products.append(product)
    
def vertical_product(number_grid, row, col, products):
    if row <= 16:

        product = 1            
        for index in range(0, 4):
            rowindex = row + index
            product *= number_grid[rowindex][col]
        
        products.append(product)
    
def SW_product(number_grid, row, col, products):
    if row <= 16 and col >= 3:
        product = 1            
        for index in range(0, 4):
            rowindex = row + index
            colindex = col - index
            product *= number_grid[rowindex][colindex]
        
        products.append(product)
    
def NE_product(number_grid, row, col, products):
    if row >= 3 and col <= 16:
        product = 1            
        for index in range(0, 4):
            rowindex = row - index
            colindex = col + index
            product *= number_grid[rowindex][colindex]
        
        products.append(product)
        
    
def get_num_divisors(triangular_number, prime_factors):
    """finds all divisors by storing factors temp list, and multiplying by prime numbers."""
    unique_primes = [] 
    
    # this loop gets only unique values in unique_primes
    for prime in prime_factors:
        if prime not in unique_primes:
            unique_primes.append(prime)
            
    factors = list(unique_primes)
    
    for prime in unique_primes:
        
        for factor in factors:
            
            candidate = prime * factor
            if candidate not in factors and triangular_number % candidate == 0:
                factors.append(candidate)
                
    factors.insert(0,1)
    num_divisors = len(factors)        
    return num_divisors, factors


def get_collatz_sequence(number):
    sequence_terminated = False
    collatz_sequence = [number]
    while not sequence_terminated:
        number = next_collatz_term(number)
        if number == 1:
            sequence_terminated = True
        collatz_sequence.append(number)
        
    return collatz_sequence
        
def next_collatz_term(n):
    '''
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)
    '''
    if  n % 2 == 0:
        n /= 2
    
    else:
        n = 3 * n + 1
 
    return n


def get_num_word_length(n, word_length_dict):
    n = str(n)
    if len(n) == 4:
        word_length = len('onethousand')
    
    elif len(n) == 3:
        word_length = get_3digit_num_word_length(n, word_length_dict)
    
    elif len(n) == 2:
        word_length = get_2digit_num_word_length(n, word_length_dict)
    
    else:
        word_length = word_length_dict[n]
    
    return word_length

def get_3digit_num_word_length(n, word_length_dict):
        first = n[0:1]
        last_two = n[1:3]
        word_length = word_length_dict[first] + word_length_dict['100']
        
        if last_two != '00':
            word_length = word_length + 3 + get_2digit_num_word_length(last_two, word_length_dict)
        
        return word_length

def get_2digit_num_word_length(n, word_length_dict):
    intn = int(n)
    if intn < 10:
        n = n[1:2]
        word_length = word_length_dict[n]
    
    elif intn < 20:
        word_length = word_length_dict[n]
    
    else:
        tens_place = n[0:1] + '0'
        ones_place = n[1:2]
        
        if ones_place == '0':
            word_length = word_length_dict[tens_place]
        else:
            word_length = word_length_dict[tens_place] + word_length_dict[ones_place]

    return word_length
    
def get_word_length_dict():
    word_length_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
                        7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',
                        12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
                        16:'sixteen', 17:'seventeen', 18: 'eighteen', 19: 'nineteen',
                        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
                        70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000: 'thousand'}
    
    list_of_indices = []
    for index in word_length_dict: 
        # change from words to the lengths of the words, and store indices in list
        # store them in a list so that it can be iterated and the dict keys can be changed
        # changing the keys to strings here will increase efficiency
        
        word_length_dict[index] = len(word_length_dict[index])
        list_of_indices.append(index)
       
    for index in list_of_indices:    
        word_length_dict[str(index)] = word_length_dict.pop(index)
    
    return word_length_dict
    

def get_greatest_sum(triangle):
    '''
    Gets the greatest possible sum out of all paths down a triangle
    Essentially, rather than going down each possible path, this
    function iterates along each row of the triangle a single time,
    and remembers the greatest possible sum at each row of the trianlge.
    '''
    current_row_sum = triangle[0]
    for rownum, row in enumerate(triangle):
        if rownum != 0: # the first row's greatest sum is just the value of the first number.
            last_row_sum = list(current_row_sum)
            current_row_sum = []
            
            for index, number in enumerate(row):
                if index == 0: # the path down the left side of the triangle
                    current_row_sum.append(last_row_sum[0] + number)
                
                elif index == len(row) - 1: # the path down the right side of the triangle
                    current_row_sum.append(last_row_sum[index - 1] + number)
                else:
                    first_value = last_row_sum[index - 1] + number
                    second_value = last_row_sum[index] + number
                    if first_value > second_value:
                        max_value = first_value
                    else:
                        max_value = second_value
                    current_row_sum.append(max_value)
                
    greatest_sum = max(current_row_sum)            
    return greatest_sum
    
def format_number_pyramid(triangle):
    """Formats a triangle to be a list of lists with no empty values"""
    triangle_as_list = triangle.split('\n')
    triangle_as_list = [row for row in triangle_as_list if row != '']
    
    for rownum, row in enumerate(triangle_as_list): # separate numbers
        triangle_as_list[rownum] = row.split(' ')
    
    formatted_triangle = []
    
    for row in triangle_as_list: # get rid of non-numbers
        row = [int(value) for value in row if value != '']
        formatted_triangle.append(row)
    
    for row in formatted_triangle: # get rid of empty rows
        if row == []: 
            formatted_triangle.remove([])
    
    return formatted_triangle


def calibrate_days(start_year):
    '''
    Gets the day for January 1 of start_year, knowing that Jan 1 1900 was a Monday
    Returns 0 for Sunday, 1 for Monday, 2 for Tuesday... 6 on Monday
    '''
    
    days_difference = 0
    
    if start_year > 1900:
        begin_year = 1900
        end_year = start_year
    
    else:
        begin_year = start_year
        end_year = 1900
        
    for year in range(begin_year, end_year):
    
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days_difference += 366
        else:
            days_difference += 365
    
    if start_year <= 1900:
        days_difference = -days_difference
    
    start_day = (days_difference + 1) % 7
    return start_day
    
def get_first_of_month_days(first_day, start_year, end_year):
    '''Days since 1 Jan 1900: each one starts with '''
    first_of_month = [first_day]
    
    for year in range(start_year, end_year + 1):
            first_of_month.append(first_of_month[-1] + 31)      # January            
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                first_of_month.append(first_of_month[-1] + 29)  # February leap year
            else:
                first_of_month.append(first_of_month[-1] + 28)  # February normal year
            first_of_month.append(first_of_month[-1] + 31)      # March
            first_of_month.append(first_of_month[-1] + 30)      # April
            first_of_month.append(first_of_month[-1] + 31)      # May
            first_of_month.append(first_of_month[-1] + 30)      # June
            first_of_month.append(first_of_month[-1] + 31)      # July
            first_of_month.append(first_of_month[-1] + 31)      # August
            first_of_month.append(first_of_month[-1] + 30)      # September
            first_of_month.append(first_of_month[-1] + 31)      # October
            first_of_month.append(first_of_month[-1] + 30)      # November
            first_of_month.append(first_of_month[-1] + 31)      # December
    
    return first_of_month
            

def shelve_primes_less_than_n(n=10000000):
    primes_less_than_n = calc_primes_less_than_n(n)
    myfile = shelve.open('primes_less_than' + str(n))
    myfile['primes_less_than' + str(n)] = primes_less_than_n
    myfile.close()
    print('Consider it shelved.')


def shelve_numbers_factors(max_num=50000):
    """Shelves numbers and their factors"""
    myfile = shelve.open('numbers_and_factors_to' + str(max_num))
    numbers_factors = get_numbers_and_factors(max_num)
    myfile['numbers_factors'] = numbers_factors
    myfile.close()
    print('Shelved numbers & factors up to {0}'.format(max_num))


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


def get_numbers_and_factors(max_num):
    '''Returns a list of tuples of number/combo pairs'''
    numbers_factors = [2, [1]] # used to store (number, factor) tuples
    primes_found = [2]
    num = 3
    while num <= max_num:

        prime_factors_of_num = get_prime_factors2(num, primes_found)
        all_num_factors = get_all_factors(num, prime_factors_of_num)
        numbers_factors.append((num,all_num_factors))
        
        num += 1
    return numbers_factors


def get_numbers_and_summed_factors(max_num):
    '''Returns a list of tuples of number/combo pairs'''
    numbers_factors = [] # used to store (number, factor) tuples
    primes_found = []
    num = 2
    while num <= max_num:

        prime_factors_of_num = get_prime_factors2(num, primes_found)
        all_num_factors = get_all_factors(num, prime_factors_of_num)
        sum_of_factors = sum(all_num_factors)
        numbers_factors.append((num,sum_of_factors))
        
        num += 1
    return numbers_factors
        
def get_all_factors(n, prime_factors):
    """Gives a list of all """
    all_factors = [1]
    for prime in prime_factors:
        if prime not in all_factors:
            all_factors.append(prime) 
    
    for prime in prime_factors:
        for factor in all_factors:
            test_factor = prime * factor
            if (n % test_factor == 0) and (test_factor not in all_factors) and (test_factor != n):
                all_factors.append(test_factor)

    all_factors.append(n)
    return all_factors
            

def get_alphabet_dict():
    alpha_dict = {}
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for index, letter in enumerate(alphabet):
        alpha_dict[letter] = index + 1 # add 1 to get 1 - 26 instead of 0 - 25
    
    return alpha_dict


def get_unique_sums(max_num, abundant_numbers):
    """
    Given a list of numbers, scrolls through the list to give all pairs of 
    unique sums.
    """
    unique_sums = set()
    
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
    total = 1 # index for num_fact
    num = 0 # index for num_fact
    
    abundant_numbers = set()
    
    for num_fact in numbers_factors:
    
        if num_fact[total] > num_fact[num]:
        
            abundant_numbers.add(num_fact[num])
    
    return abundant_numbers


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

def get_digit(n, digit):
    """ Return digit of n. digit of 0 is for ones place, 1 for tens, etc. """
    n = str(n)
    index = len(n) - (digit + 1)
    return int(n[index])

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


def get_coin_total(coins, target, so_far, coin):
    
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

def is_pandigital_generator(low=1, high=9):
    """ Test whether numbers are low-high pandigital 
    
    Args:
        low: lower bound for pandigitality
        high: upper bound for pandigitality
    
    """
    
    pandigital_digits = set(str(i) for i in range(low, high + 1))
    num_digits_required = 1 + high - low
    
    def is_pandigital(numbers):
        digits = copy.copy(pandigital_digits)
        num_digits = sum(int(log(n,10) + 1) for n in numbers)    
        if num_digits != num_digits_required: 
            return False
        
        for number in numbers:
            for digit in str(number):
                try:
                    digits.remove(digit)
                except KeyError:
                    return False
                
        return True
    
    return is_pandigital
    
    
    
def yield_permutations_maker(low, high):
    
    def yield_permutations(string_as_int):
        for index1 in range(1,high - low):
            for index2 in range(index1 + 1, high):
                num1 = int(string_as_int[:index1])
                num2 = int(string_as_int[index1:index2])
                num3 = int(string_as_int[index2:]) 
                
                yield (num1, num2, num3)
                
    return yield_permutations

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

def circularize(number):
    '''
    Yield all circular permutations of a number.  
    For instance, 197 would return 197, 971, and 719.
    '''
    
    number = str(number)
    num_digits = len(number)

    circulars = []
    for char_index in range(num_digits):
        if number[char_index] == 0:
            continue
        new_num = number[char_index:num_digits] + number[0:char_index]
        #yield int(new_num)
        circulars.append(int(new_num))
    
    return circulars
        

def base10to2helper(number, digits_needed, so_far):
    if digits_needed == 1:
        if number == 0:
            return so_far + '0'
        else:
            return so_far + '1'
        
    if 2 ** (digits_needed - 1) <= number:
        so_far += '1'
        number -= 2 ** (digits_needed - 1)
    else:
        so_far += '0'
    
    return base10to2helper(number, digits_needed - 1, so_far)
    
def base10to2(number):
    '''
    returns the base2 representation, as a string.
    '''
    digits_needed = int(log(number) / log(2)) + 1    
    so_far = ''
    
    return base10to2helper(number, digits_needed, so_far)
    
def ispalindrome(astring):
    return astring == astring[::-1]
        

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]    

def is_square(number):
    sqrtnum = sqrt(number)
    return sqrtnum == int(sqrtnum)
    
def truncate(number):
    '''
    returns a list of truncated numbers, based on the number given.
    It truncates from left to right, then from right to left.
    for instance, if number is 3797, it returns
    [3797, 797, 97, 7, 379, 37, 3], although not in that order.
    '''
    
    truncated_numbers = [number]
    number = str(number)
    length = len(number)
    
    for position in range(1, length):
        
        # take away the right digits
        truncated_numbers.append(int(number[0: length - position]))
        
        # take away the left digits
        truncated_numbers.append(int(number[position:length]))
    
    return truncated_numbers

def get_num_digits(number):
    """ Return the number of digits in number """
    return len(str(number))
    
def right_triangle_combinations(p):
    """For a triangle with perimeter p, yield all solutions of right triangles."""
    # make side1 always be the shortest of the three sides
    side1_max = p // 3
    side2_max = (p * 2) // 3
    for side1 in range(1, side1_max):
        for side2 in range(side1 + 1, side2_max):
            side3 = p - (side1 + side2)
            if side1**2 + side2**2 == side3**2:
                yield side1, side2, side3
