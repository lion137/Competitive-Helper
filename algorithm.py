# Module with various utilities to competitive mathematics/programming.
# copyleft 2018 lion137
# Sources: P. Norvig: Pytudes, Stackoverflow, Wikipedia
# http://en.literateprograms.org/Miller-Rabin_primality_test_(Python).


from operator import mul
import random
from functools import reduce
from fractions import Fraction
from collections import Counter
from itertools import repeat, product
from math import log, pow, gcd


class Matrix:
	
	a = None
	
	def __init__(self, n, xs=None):
		arr=[[0 for x in range(n)] for x in range(n)]
		self.a = arr
		if xs:
			for i in range(len(xs)):
				self.a[i] = xs[i]
	
	def zero(self):
		return Matrix(len(self)) 
			
	def id(self):
		length = len(self)
		arr = [[0 for x in range(length)] for x in range(length)]
		for i in range(length):
			for j in range(length):
				if ( i == j):
					arr[i][j] = 1
		return Matrix(length, arr)
	
	def __repr__(self):
		return str(self.a)
	
	def __eq__(self, other):
		return self.a == other.a
	
	def set_at(self, e, i, j):
		self.a[i][j] = e
	
	def get_at(self, i, j):
		return self.a[i][j]
	
	def __mul__(self, other):
		
		length = len(self.a[0])
		ll = [0] * length
		lll = []
		for _ in range(length):
			lll.append(ll)
		C = Matrix(length)
		
		for i in range(length):
			for j in range(length):
				s = 0
				for k in range(length):
					s = s + self.a[i][k] * other.a[k][j]
				C.a[i][j] = s
		return C
	
	def mod_mul_mat(self, other, m):
		
		length = len(self.a[0])
		ll = [0] * length
		lll = []
		for _ in range(length):
			lll.append(ll)
		C = Matrix(length)
		
		for i in range(length):
			for j in range(length):
				s = 0
				for k in range(length):
					s = (s +  ( ((self.a[i][k] % m) *  (other.a[k][j] % m)) % m ) ) % m
				C.a[i][j] = s
		return C
	
	def __len__(self):
		return len(self.a)
	
	def __mod__(self, m):
		length = len(self)
		for i in range(length):
			for j in range(length):
				self.a[i][j] = self.a[i][j] % m
		return self


# General purpose internal functions

def zero(a):
	if isinstance(a, int) or isinstance(a, float): return 0
	if isinstance(a, complex): return 0 +0j
	if isinstance(a, Matrix): return a.zero()

def identity(a):
	if isinstance(a, int) or isinstance(a, float): return 1
	if isinstance(a, complex): return 1 +0j
	if isinstance(a, Matrix): return a.id()

def mod(e, m):
	if isinstance(e, int): return e % m
	if isinstance(e, Matrix): return e % m

def odd(n):
	return n % 2 == 1
	
def half(a):
	if isinstance(a, complex): return a / 2
	if isinstance(a, int): return a >> 1

def mod_mul(a, b, m):
	if isinstance(a, int): return ( (a % m) * (b % m)) % m
	if isinstance(a, Matrix): return a.mod_mul_mat(b, m)

def mat_vec(a, xs):
	"""Square matrix times vector multiplication"""
	limit = len(xs)
	result = [0] * limit
	for i in range(limit):
		s = zero(xs[0])
		for k in range(limit):
			s = s + a.a[i][k] * xs[k]
		result[i] = s
	return result 

def mat_vec_mod(a, xs, m):
	limit = len(xs)
	result = [0] * limit
	for i in range(limit):
		s = zero(xs[0])
		for k in range(limit):
			s = (s + mod_mul(a.a[i][k],  xs[k], m) ) % m
		result[i] = s
	return result
	

#  Prime Factoroization, Number Theoretic, internal  functions

def sqrt_int(n):
    "Integer square root (rounds down)."
    return int(n ** 0.5)

def mult(nums):
	result = 1
	for n in nums:
		result *= n
	return result

# Functions

def power(x, n, f=mul):
	"""Takes regular type, x (square matrix, number or complex)
	and without specified f, returns its power to n"""
	if n == 0: return identity(x)
	y = identity(x)
	while n > 1:
		if not odd(n):
			x = f(x, x)
			n = half(n)
		else:
			y = f(x, y)
			x = f(x, x)
			n = (n - 1) // 2
	return f(x, y)
	
def pow_mod(a, n, m, f=mod_mul):
	"""Takes a regular type element a (matrices and numbers), n, m 
	   and f (operator) returns a to power n modulo m.
	   Default f is multiplication modulo of numbers and matrices"""
	if 1 == m: return zero(a)
	if a == zero(a): return zero(a)
	result = identity(a)
	a = mod(a, m)
	while n > 0:
		if odd(n):
			result = f(a, result, m)
		n = half(n)
		a = f(a, a, m)
	return result

def recurrence(n, a_vec, c_vec):
	"""Computes nth value of recurrence, 
	for info about a_vec and c_vec see: 
	https://github.com/lion137/Linear_Recurrence_Solver"""
	limit = len(a_vec)
	A = Matrix(limit)
	for i in range(limit):
		A.a[0][i] = a_vec[i]
	for i in range(1, limit):
		for j in range(limit):
			if i - j == 1:
				A.a[i][j] = 1
	if n < len(c_vec): return c_vec[n]
	c_vec = c_vec[::-1]
	return mat_vec(power(A, n + 1 - limit), c_vec)[0]
	
	
def recurrence_mod(n, a_vec, c_vec, m):
	"""Computes the nth value of the given recurrence
	modulo m, see: https://github.com/lion137/Linear_Recurrence_Solver"""
	limit = len(a_vec)
	A = Matrix(limit)
	for i in range(limit):
		A.a[0][i] = a_vec[i]
	for i in range(1, limit):
		for j in range(limit):
			if i - j == 1:
				A.a[i][j] = 1
	if n < len(c_vec): return c_vec[n]
	c_vec = c_vec[::-1]
	return mat_vec_mod(pow_mod(A, n + 1 - limit, m), c_vec, m)[0]

# Number Theoretic, Primes

def is_prime(n):
    """
    Test if prime, Miller Rabin
	"""
    if n == 1: return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


def miller_rabin_pass(a, s, d, n): # is_prime helper
    a_to_power = pow_mod(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def sieve(n):
	"""Create an iterable generator of primes, with initial cache of all primes <= n."""
	N = n // 2 
	_sieve = [True] * N
	for i in range(3, sqrt_int(n) + 1, 2):
		if _sieve[i // 2]: # i is prime
			# Mark start, start + i, start + 2i, ... as non-prime
			start = i ** 2 // 2
			_sieve[start::i] = repeat(False, len(range(start, N, i)))
	_list = [2] + [2*i+1 for i in range(1, N) if _sieve[i]]
	_set  = set(_list)
	maxn  = n # We have tested for all primes < self.maxn
	return [_list, _set, n]

def primes(n):
	"""Primes up tu n"""
	return sieve(n)[0]

milion = 1000000
prime_nums = sieve(10 * milion)

def factorize(n):
	"""Prime factorization of 1 < n < 10^12"""
	result = []
	if n >= 2 * milion:
		for p in prime_nums[0]:
			while n % p == 0:
				result.append(p)
				n //= p
			if n < 2 * milion:
				break
			if is_prime(n):
				result.append(n)
				return result
	for p in prime_nums[0]:
		while n % p == 0:
			result.append(p)
			n //= p
	return result

def distinct_factors(n):
	return set(factorize(n))

def totient(n):
	"""Eulers Totient function: https://en.wikipedia.org/wiki/Euler's_totient_function"""
	return int( n * mult(1 - Fraction(1, p) for p in set(factorize(n))))

def ndivisors(n):
	"""Returns number of divisors"""
	exps = Counter(factorize(n)).values()
	return mult(a + 1 for a in exps)

def divisors(n):
	"""Returns the all divisors of n"""
	if n == 1: return 1
	factors = list(distinct_factors(n))
	length = int(log(n, min(factors))) + 1
	comb = [item for item in product(list(range(length + 1)), repeat=len(factors))]
	result = []
	for e in comb:
		tmp = []
		for p, c in zip(factors, e):
			tmp.append(int(pow(p, c)))
		m = mult(tmp)
		if m <= n // 2 and n % m == 0:
			result.append(m)
	result = list(set(result))
	result.append(n)
	result.sort()
	return result

def sdivisors(n):
	"""Returns sum of proper divisors, less < n"""
	return sum(divisors(n)) - n


def lcm(a, b):
	"""Least Common Multiple of a, b"""
	return abs(a * b) // gcd(a, b)
