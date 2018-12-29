
### Competitive-Helper
Various utilities to help with competitive programming/math. Including, solving recurrences,    
from here: https://github.com/lion137/Linear_Recurrence_Solver.      
Before starts, run prime sieve to 10 milions - to reasonably fast factorize numbers up to ```10^16```. No dependencies, just standard library.              
Functions:
- ```is_prime```;    
- ```divisors(n)``` - all divisors of ```n```;    
-  ```primes(n)``` - primes up to ```n```;    
- ```factorize(n)``` - factors of ```n```;     
- ```distinct_factors(n)```;     
- ```totient(n)``` - Eulers Totient function;     
- ```ndivisors(n)``` - number of divisors of ```n```;     
- ```sdivisors(n)``` - sum of proper divisors;    
- ```lcm(n, m)``` - Least Common Multiple of ```n```, ```m```;     
- ```recurrence(n, vec, vec1)``` - solves recurrence: https://github.com/lion137/Linear_Recurrence_Solver;     
- ```recurrence_mod(n, vec, vec1, mod)``` - solves recurrence modulo;     
- ```pow_mod(a, n, m)``` - power of ```a``` to ```n``` modulo ```m```.      
- ```reduce_series(op, f, start, end, e=None)``` - applies an op to the series f, from start to the end exclusive, read the docs for more. Ex:    
  ```reduce_series(add, lambda x: 1 / n, 1, 5) = 2.083333333333333``` - Harmonic series: https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)     
     
One can, also, rise a matrix to some power ```n >= 0``` .     
Any suggestions, bugs, comment here or on: https://lion137.blogspot.com/2018/12/competitive-math-helper.html     
Could be use directly in code or as a quick check in console:    
<a href="https://asciinema.org/a/218695" target="_blank"><img src="https://asciinema.org/a/218695.svg" /></a>



