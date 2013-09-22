
"""
Solutions to problems on Project Euler
"""
__author__ = 'Cody Piersall'

import copy
import itertools
import functools
import shelve
from math import sqrt, factorial, log

SHELVED_FILE = "numbers_and_factors"


def divisible_by(n, numbers):
    """for i in range(1,n), return list of numbers divisible by any number in numbers """
    return [i for i in range(1,n) if any(i % a == 0 for a in numbers)]
    

def clean_fib_numbers(fibonacci_numbers, divisor=2):
    '''
    returns a list from a list of numbers divisible by divisor.
    '''
    divisible_fib_nums = []
    for number in fibonacci_numbers:
        if number % divisor == 0:
            divisible_fib_nums.append(number)
    
    return divisible_fib_nums


def fibonacci(maxnum):
    """
    Calculates the numbers in the fibonacci sequence <= maxnum
    """
    fib_nums = [1,2]
    fib_nums_max = fib_nums[-1]
    
    while fib_nums_max <= maxnum:
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)
        fib_nums_max = fib_nums[-1]
        
    # The above while loop added one number too many; time to take it off.
    fib_nums.pop()
    return fib_nums


def get_prime_factors2(n, primes_found):
    '''
    Given a list of prime numbers < n, return all of n's prime factors
    '''
    factors = []
    for prime in primes_found:
            while n % prime == 0:
                factors.append(prime)
                n /= prime
            
    if n != 1 and n not in primes_found:
        primes_found.append(n)
        
    return factors
            

def get_prime_factors(number):
    '''
    returns a list of prime factors
    '''
    divisors = []
    divided_number = number
    while divided_number != 1:
        divisor = 2
        
        while divisor <= divided_number:
            
            if divided_number % divisor == 0:
                divisors.append(divisor)
                divided_number = divided_number / divisor
            
            else:
                divisor += 1
    print('The divisoros of %s is %s' %(number, divisors))
    return divisors


def check_if_palindrome(number):
    number = str(number)
    backwards_number = number[::-1]
    if number == backwards_number:
        is_palindrome = True
    else:
        is_palindrome = False
    return is_palindrome  
        

def sum_squares(number):
    sum_of_squares = 0
    for num in range(1, number + 1):
        sum_of_squares += num ** 2
    return sum_of_squares
        
def square_sum(number):
    square_of_sum = sum(range(1, number + 1)) ** 2
    return square_of_sum


def calc_nth_prime(nth_prime):
    """
    Method calculates the nth prime number.  It stores each found prime number into
    a list, and only divides the current number being tested by the previously found
    prime numbers.
    """
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


def prob8():
    '''
    Find the greatest product of five consecutive digits in the 1000-digit number.
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    '''
    number_string = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    products = analyze_string(number_string)
    max_product = max(products)
    print('the greatest product of five consecutive digits in the 1000-digit number is %s' % max_product)
    

def analyze_string(string, consecutive_digits=5):
    """Multiplies every group of 5 consecutive numbers together, stores results in a list."""
    string_length = len(string)
    iterations_needed = string_length - consecutive_digits
    
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


def prob9(number):
    """
    A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

    a**2 + b**2 = c**2
    For example, 32 + 42 = 9 + 16 = 25 = 5**2.
    
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    
    max_value = int(number / 2) # add 1 because int() floors the float, add another because range needs 1 more than I would think.
    
    for a in range(1,max_value):
        for b in range(1, max_value):
            for c in range(1, max_value):
                if c <= a or c <= b:
                    pass
                else:
                    if a ** 2 + b ** 2 == c ** 2:
                        if a + b + c == number:
                            print('The product of the Pythagorean triplet which adds to %s is %d' % (number, a*b*c))
                            break
                

def prob10(nmax):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """

    prime_nums = calc_primes_less_than_n(nmax)
    print('The sum of the primes less than %s is %s' % (nmax, sum(prime_nums)))
    

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
 
 
def prob11():
    '''
    In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

    What is the greatest product of four adjacent numbers in any direction 
    (up, down, left, right, or diagonally) in the 20x20 grid?
    '''
    string_of_numbers = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
    
    number_grid = string_of_numbers.split('\n')
    number_grid.remove('') # from the first '\n'
    
    
    for row in range(0, len(number_grid)):
        number_grid[row] = number_grid[row].split(' ')
        for number in number_grid[row]:
            number = int(number)
    
    number_grid = [[int(column) for column in row] for row in number_grid]
    
    products = get_products(number_grid)

    print('The largest product of 4 numbers in the 20x20 grid is %s' % max(products))


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
        
    
def prob12(num_divisors_needed):  
    """
    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    
    Let us list the factors of the first seven triangle numbers:
    
    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.
    
    What is the value of the first triangle number to have over five hundred divisors?
    """
    
    # Set up for while loop
    number_found = False
    triangular_num_increment = 1 # would be 1 if incremented at top of while loop
    triangular_number = 1
    
    while(not number_found):
       
        prime_factors = get_prime_factors(triangular_number)
        num_divisors, factors = get_num_divisors(triangular_number, prime_factors)
        
        if num_divisors > num_divisors_needed:
            number_found = True
            print('The first triangular number with over %s divisors is %s' % (num_divisors_needed, triangular_number))
        
        else:
            triangular_num_increment += 1
            triangular_number += triangular_num_increment


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


def prob13():
    """
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    """
    number_as_text = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""

    list_of_numbers = number_as_text.split("\n")
    list_of_numbers = [int(num) for num in list_of_numbers]
    sum_of_nums = sum(list_of_numbers)
    sum_of_nums10 = str(sum_of_nums)[0:10]
    print('The first 10 digits of the sum of those bunches of numbers is %s' % sum_of_nums10)


def prob14(maxnum):
    """
    The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)
    
    Using the rule above and starting with 13, we generate the following sequence:
    
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), it is thought that 
    all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?    
    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    """
    My idea for solving it is this:  start at one million, do the series, and store
    tuples for how many iterations are left.  
    For the example above, the algorithm would give this:
    (13, 9), (40, 8) (20, 7), (10, 6), ..., (2, 1), (1, 0)
    """
    longest_sequence = []
    minnum = int(maxnum / 2) # any number less than half of the max number will be reached with one more entry by dividing by two.
    
    for number in range(minnum,maxnum):
        if number not in longest_sequence:
            temp_sequence = get_collatz_sequence(number)
            if len(temp_sequence) > len(longest_sequence):
                longest_sequence = list(temp_sequence)
    starting_number = longest_sequence[0]
    
    print('Of numbers < %s, The starting number with the longest chain is %s. It has %s terms.' % (maxnum, starting_number, len(longest_sequence)))
    

def prob15(num_rows, num_columns):
    """
    Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
    How many routes are there through a 20x20 grid?
    """
    '''
    One way to represent moving along the grid is by writing moves to the right as R and
    moves down as D. Because there can be no backtracking, there must be exactly 20 moves 
    to the right and 20 moves down. These moves can be in any order; so the problem is 
    equivalent to how many unique ways to organize 20 Rs and 20 Ds.  One solution is
    RRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDD; another is
    RRRRRRRRRRRRRRRRRRRDRDDDDDDDDDDDDDDDDDDD; another is
    RRRRRRRRRRRRRRRRRRRDDRDDDDDDDDDDDDDDDDDD and so on.
    
    Conceptually, this is how I understand solving this: give each R and D a unique ID; 
    let them be the numbers 1-40.  There are 40! ways to order their IDs; one possible solution is
    RRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDD
    0123456789abcdefghijklmnopqrstuvwxyzABCD
    
    But there are many ways to order the IDs to achieve this unique combination of Rs and Ds.  Because
    There are 20 Rs (each with a unique ID), there are 20! ways to organize the Rs for this combination
    of Rs and Ds.  Similarly there are 20! ways to organize the Ds.  So, for this combination of Rs and
    Ds, there are 20! * 20! unique combinations of their IDs.
    
    To get the unique combinations of Rs and Ds, we can find the unique combinations of IDs and divide
    by the number of ways to order the IDs of the Rs and the IDs of the Ds.  This gives us
    
                      (R + D)!
    Combinations = -------------
                      R! * D!
                      
    which can be generalized for an m x n grid to 
    Combinations = (m + n)! / (m! * n!)
    '''  
    unique_combinations = factorial(num_rows + num_columns) / (factorial(num_rows) * factorial(num_columns))
    print('There are %s unique ways to get from one corner to its opposite on a %sx%s grid.' %(unique_combinations, num_rows, num_columns))


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


def prob16(base, exp):
    """Sum of the digits of 2 ** 1000"""

    two_to_thousand = base ** exp
    two_to_thousand = str(two_to_thousand)
    sum_ = 0
    for digit in two_to_thousand:
        digit = int(digit)
        sum_ += digit
    print('The sum of the digits of %s ** %s = %s' % (base, exp, sum_))


def prob17(minnum, maxnum):
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
    there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
    how many letters would be used?
    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
    contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use 
    of "and" when writing out numbers is in compliance with British usage.
    """
    word_length_dict = get_word_length_dict()
    total_length = 0
    for n in range(minnum,maxnum + 1):
        total_length += get_num_word_length(n, word_length_dict)
    print('Writing out all numbers from %s to %s takes %s letters' % (minnum, maxnum, total_length))

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
    

def prob18():
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
       3
      7 4
     2 4 6
    8 5 9 3
    That is, 3 + 7 + 4 + 9 = 23.
    Find the maximum total from top to bottom of the triangle below:
    """
    raw_triangle = '''
                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    '''
    triangle = format_triangle(raw_triangle)
    greatest_sum = get_greatest_sum(triangle)
    print('The greatest sum out of any path is %s' % greatest_sum)
    
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
    
def format_triangle(triangle):
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


def prob19(start_year, end_year, day_of_week='Sunday'):
    """
    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """
    
    days_dict ={'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
    day_ID = days_dict[day_of_week]
    
    first_day_ID = calibrate_days(start_year) # returns day ID for first day of year
    
    # list_of_days treats every year like a leap year because it doesn't matter how many days are in 
    # the list as long as the correct days are in first_of_month
        
    list_of_days = [day for day in range(day_ID, 366 * (end_year - start_year + 1), 7)]
    
    first_of_month = get_first_of_month_days(first_day_ID, start_year, end_year)
    
    num_first_days = 0
    for day in first_of_month:
        if day in list_of_days:
            num_first_days += 1
    
    print('%s months from %s to %s began with a %s' % (num_first_days, start_year, end_year, day_of_week))

def calibrate_days(start_year):
    '''
    Gets the day for January 1 of start_year, knowing that Jan 1 1900 was a Monday
    Returns 0 for Sunday, 1 for Monday, 2 for Tuesday... 6 on Monday
    '''
    
    days_difference = 0
    first_day_of_1900 = 1 # Monday
    
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
    print('the first day of %s was %s' %(start_year,start_day))
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
            

def prob20(number):
    """Find the sum of digits in 100!"""
    fact = factorial(number)
    sum_of_digits = sum([int(digit) for digit in str(fact)])
    print('The sum of the digits of %s! is %s' % (number, sum_of_digits))


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
    total = 1 # index for num_fact
    num = 0 # index for num_fact
    
    abundant_numbers = set()
    
    for num_fact in numbers_factors:
    
        if num_fact[total] > num_fact[num]:
        
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

def prob32(low=1, high=9):
    """
    We shall say that an n-digit number is pandigital if it makes use 
    of all the digits 1 to n exactly once; for example, the 5-digit 
    number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 * 186 = 7254, 
    containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product 
    identity can be written as a 1 through 9 pandigital.
    
    HINT: Some products can be obtained in more than one way so be 
    sure to only include it once in your sum.
    """
    
    pandigital_numbers = ''
    for number in range(low, high + 1):
        pandigital_numbers += str(number)
    yield_permutations = yield_permutations_maker(low, high)
    products = set()
    for permutation in itertools.permutations(pandigital_numbers, high - low + 1):
        p = ''.join(permutation)
        for num1, num2, num3 in yield_permutations(p):
            if num1 * num2 == num3: products.add(num3)
    
    print(sum(products))
    
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

def prob35(maxnum=1000000):
    '''
    The number, 197, is called a circular prime because all 
    rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 
    100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    
    How many circular primes are there below one million?
    '''
    
    primes_file = shelve.open('primes_less_than1000000')
    primes = primes_file["primes_less_than1000000"]
    primes_file.close()
    
    circular_primes = set()
    
    for number in range(maxnum):
        
        if number in primes:
            rotations = circularize(number)
            
            if all((i in primes) for i in rotations):
    
                for rotation in rotations:
                    circular_primes.add(rotation)
            
    print(circular_primes)
    print('the answer is {0}'.format(len(circular_primes)))
    
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
        

def prob36(maxnum):
    '''
    The decimal number, 585 = 1001001001 (binary), is palindromic 
    in both bases.

    Find the sum of all numbers, less than one million, which are 
    palindromic in base 10 and base 2.
    
    (Please note that the palindromic number, in either base, 
    may not include leading zeros.)
    '''
    nums_found = []
    for number in range(1, maxnum):
        
        # get rid of all numbers end with an even number
        if number % 2 != 0 and ispalindrome(str(number)):
            binary = base10to2(number)
            if ispalindrome(binary):
                nums_found.append(number)
    print('All palindromes < {0}:\n{1}'.format(maxnum, nums_found))
    print('Their sum: {0}'.format(sum(nums_found)))
    
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
    if astring == astring[::-1]:
        return True
    else:
        return False
    
    
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
    
    # pull the primes from the file.
    primes_file = shelve.open("primes_less_than1000000")
    primes = primes_file["primes_less_than1000000"]
    primes_file.close()
    
    # don't look for numbers that are too small.
    number = 11
    numfound = 0
    
    truncatable_primes = []
    
    while numfound < 11 and number < 1000000:
        
        # don't check non-prime numbers
        if number in primes:
            truncations = truncate(number)
            
            if all(num in primes for num in truncations):
                truncatable_primes.append(number)
                numfound += 1
                
        number += 1
    
    total = sum(truncatable_primes)
    
    print('The truncatable primes are {0}.'.format(truncatable_primes))
    print('Their total is {0}'.format(total))
    
    
def truncate(number):
    '''
    returns a list of truncated numbers, based on the number given.
    It truncates from left to right, then from right to left.
    for instance, if number is 3797, it returns
    [3797, 797, 97, 7, 379, 37, 3], although not in that order.
    '''
    
    number = str(number)
    num_length = len(number)
    truncated_numbers = [int(number)]
    
    for position in range(1, num_length):
        
        # take away the right digits
        truncated_numbers.append(int(number[0: num_length - position]))
        
        # take away the left digits
        truncated_numbers.append(int(number[position:num_length]))
    
    return truncated_numbers

def get_num_digits(number, base=10):
    """ Return the number of digits in number """
    return int(log(number, base) + 1)
    
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
    
    largest = ''
    is_pandigital = is_pandigital_generator(1, 9)

    for n in range(1, 100000):
        num_digits = get_num_digits(n)
        numbers = [n]
        multiplier = 2
        
        while num_digits < 9:
            new_num = n * multiplier
            numbers.append(new_num)
            num_digits += get_num_digits(new_num)
            
        if num_digits == 9 and is_pandigital(numbers):
            num_as_string = ''.join(str(num) for num in numbers)
            
            if num_as_string > largest:
                largest = num_as_string
    
    print(largest)
    
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

def prob39(max_perimeter=1000):
    '''
    If p is the perimeter of a right angle triangle with integral 
    length sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p < 1000, is the number of solutions maximised?
    '''
    
    max_found = 0
    p_max = 1
    for perimeter in range(12, max_perimeter):
        num_found = len(list(right_triangle_combinations(perimeter)))
        if num_found > max_found:
            max_found = num_found
            p_max = perimeter
    
    print('Found {0} solutions with perimeter of {1}'.format(max_found, p_max))


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
    product = lambda a, b: a * b
    a = '.' + ''.join(str(i) for i in range(1, 500000))
    digits = (int(a[10 ** i]) for i in range(7))
    print(functools.reduce(product, digits))

def prob41():
    """
    We shall say that an n-digit number is pandigital if it makes use of all 
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital 
    and is also prime.
    
    What is the largest n-digit pandigital prime that exists?
    """

def test_truncate():
    print(truncate(3797))

#test_truncate()
if __name__ == "__main__":
#    prob1(1000)
#    prob2(4000000)
#    prob3(0) 
#    prob4()
#    prob5(20)
#    prob6(100) 
#    prob7(1001)
#    prob8()
#    prob9(1000)
#    prob10(20000)
#    prob11()
#    prob12(500)
#    prob13()
#    prob14(1000)
#    prob15(20, 20)
#    prob16(2, 100)
#    prob17(1, 1000)
#    prob18()
#    prob19(1901, 2000, 'Monday')
#    prob20(100)
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
#    prob32()
#    prob33()
#    prob34()
#    prob35(1000000)
#    prob36(1000000)
#    prob37()
#    prob38()
#    prob39()
    prob40()
#    test_prob31()
#    shelve_primes_less_than_n(10000000)
    pass