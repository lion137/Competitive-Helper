# tests

from algorithm import *


def tests():
	
	print("Test Zero int")
	assert zero(123) == 0
	
	print("Test Zero float")
	assert zero(123.1) == 0
	
	print("Test Zero complex")
	assert zero(1 + 2j) == 0 + 0j
	
	print("Test Zero matrix")
	m1 = Matrix(2, [[1, 1], [2, 3]])
	zer = Matrix(2);
	assert m1.zero() == zer
	
	print("Test Matrix identity id")
	m1 = Matrix(2, [[1, 1], [2, 3]])
	m2 = Matrix(2, [[1, 0], [0, 1]])
	assert m1.id() == m2
	
	print("Test Matrix Multiplication")
	m0 = Matrix(2, [[1, 1], [1, 1]])
	m1 = Matrix(2, [[1, 1], [1, 1]])
	m2 = Matrix(2, [[2, 2], [2, 2]])
	assert m0 * m1 == m2
	assert m0.id() * m0.id() == m2.id()
	
	print("Test Matrix Mod")
	m0 = Matrix(2, [ [2, 7], [11, 23] ])
	m1 = Matrix(2, [ [2, 2], [1, 3] ])
	assert m0 % 5 == m1
	
	print("Test Identity int")
	assert identity(23) == 1
	
	print("Test Identity float")
	assert identity(23.01) == 1
	
	print("Test Identity complex")
	assert identity(23 + 23j) == complex(1)
	
	print("Test Identity Matrix")
	m0 = Matrix(2, [ [2, 7], [11, 23] ])
	assert identity(m0) == m0.id()
	
	print("Test Modulo in int")
	assert mod(23, 5) == 3
	
	print("Test Modulo Matgrix")
	m0 = Matrix(2, [ [2, 7], [11, 23] ])
	m1 = Matrix(2, [ [2, 2], [1, 3] ])
	assert mod(m0, 5) == m1
	
	print("Test Odd")
	assert odd(3) == True
	assert odd(2) == False
	
	print("Test half Complex")
	assert half(2 + 2j) == 1 + 1j
	
	print("Test Modulo Mul int")
	assert mod_mul(5, 7, 3) == 2
	
	print("Test Modulo Mul Matrix")
	m0 = Matrix(2, [ [2, 4], [7, 3] ])
	m1 = Matrix(2, [ [1, 2], [3, 4] ])
	m2 = Matrix(2, [ [4, 0], [1, 1] ])
	assert mod_mul(m0, m1, 5) == m2
	
	
	print("Test Power Modulo in Inegers")
	assert pow_mod(2, 10, 1000) == 24
	assert pow_mod(3, 3, 5) == 2
	
	print("Test Power Modulo Matrix")
	m0 = Matrix(2, [ [2, 4], [7, 3] ])
	m1 = Matrix(2, [ [2, 0], [0, 2] ])
	m = Matrix(2, [ [1, 1], [1, 0] ])
	assert pow_mod(m0, 2, 5) == m1
	assert pow_mod(m, 1234567891011, 1000000007).a[0][1] == 316399615 # Fibonacci
	
	print ("Test Power in integers")
	assert power(2, 3) == 8
	assert power(2, 0) == 1
	assert power(2, 1) == 2
	assert power(3, 5) == 243
	
	
	print ("Test Power in Matrices")
	m0 = Matrix(2, [ [2, 4], [7, 3] ])
	m1 = Matrix(2, [ [32, 20], [35, 37] ])
	m_id = Matrix(2, [[1, 0], [0, 1]])
	assert power(m0, 2) == m1
	assert power(m0, 0) == identity(m0)
	assert power(m0, 1) == m0
	assert power(m_id, 1000000) == m_id
	
	print ("Matrix times Vector")
	m_id = Matrix(2, [[1, 0], [0, 1]])
	m0 = Matrix(2, [[1, 2], [3, 4]])
	assert mat_vec(m_id, [1, 1]) == [1, 1]
	assert mat_vec(m0, [1, 2]) == [5, 11]
	
	print ("Test Recurrence Solver in Integers")
	assert recurrence(0, [1, 1], [0, 1]) == 0
	assert recurrence(1, [1, 1], [0, 1]) == 1
	assert recurrence(7, [1, 1], [0, 1]) == 13
	
	# Recurrence: f(0) = 0, f(1) = 1, f(2) = 2
	# f(n) = 2f(n - 1) + 3f(n - 3) 
	def f(n):
		if n == 0: return 0
		elif n == 1: return 1
		elif n == 2: return 2
		else:
			return 2 * f(n - 1) + 3 * f(n - 3)
			 
	assert recurrence (13, [2, 0, 3], [0, 1, 2]) == f(13)
	assert recurrence (0, [2, 0, 3], [0, 1, 2]) == f(0)
	assert recurrence (1, [2, 0, 3], [0, 1, 2]) == f(1)
	assert recurrence (2, [2, 0, 3], [0, 1, 2]) == f(2)
	
	print ("Test Matrix Vector Multiplication Modulo")
	m_id = Matrix(2, [[1, 0], [0, 1]])
	m0 = Matrix(2, [[1, 2], [3, 4]])
	assert mat_vec_mod(m0, [1, 2], 1) == [0, 0]
	assert mat_vec_mod(m0, [1, 2], 2) == [1, 1]
	assert mat_vec_mod(m0, [1, 2], 7) == [5, 4]
	assert mat_vec_mod(m0, [1, 2], 20) == [5, 11]
	
	print ("Test Recurrence Modulo")
	def fibo(n):
		a, b = 0, 1
		while n > 0:
			a, b = b, a + b
			n -= 1
		return a
	par = 7
	assert fibo(par) == 13
	assert recurrence_mod(13, [1, 1], [0, 1], 13) == fibo(13) % 13
	assert recurrence_mod(150, [1, 1], [0, 1], 100007) == fibo(150) % 100007
	
	print ("")
	print ("Primes, Number Theory Tests")
	
	print ("Prime Sieve Tests")
	primes = sieve(10)
	assert primes[0] == [2, 3, 5, 7]
	assert primes[1] == {2, 3, 5, 7}
	assert primes[2] == 10
	
	print ("Test is_prime")
	assert is_prime(1) == False
	assert is_prime(42) == False
	assert is_prime(2) == True
	assert is_prime(3) == True
	assert is_prime(1000000) == False
	assert is_prime(162259276829213363391578010288127) == True
	
	print ("Test Factorization")
	assert factorize(3000000) == [2, 2, 2, 2, 2, 2, 3, 5, 5, 5, 5, 5, 5]
	assert factorize(1) == []
	assert factorize(2) == [2]
	assert factorize(35) == [5, 7]
	assert factorize(12345678910) == [2, 5, 1234567891]
	
	print("Test Totient Function")
	assert totient(100) == 40
	assert totient(1) == 1
	assert totient(137) == 136
	assert totient(13) == 12
	assert totient(1234567890) == 329040288

	print ("Test Number Of Divisors")
	assert ndivisors(12) == 6
	assert ndivisors(7) == 2

	
	print("Test Divisors")
	assert divisors(1) == 1
	assert divisors(2) == [1, 2]
	assert divisors(12) == [1, 2, 3, 4, 6, 12]
	assert divisors(137) == [1, 137]
	assert divisors(2048) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
	assert len(divisors(2048)) == 12
	assert len(divisors(100)) == 9
	assert divisors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
	
	print ("Test Sum of Proper Divisors")
	assert sdivisors(12) == 16
	assert sdivisors(137) == 1
	assert sdivisors(100) == 117
	assert sdivisors(284) == 220
	assert sdivisors(220) == 284
	
	print ("Test of Least Common Multiple lcm")
	assert lcm(21, 6) == 42
	assert lcm(3, 3) == 3
	
	
	
tests()










