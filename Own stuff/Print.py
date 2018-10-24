"""Print"""

from operator import floordiv, mod

def divide_exact(n, d):
	"""Returns the quotient and remainder 
	of dividing N by D.

	>>> q, r = divide_exact(2018, 10)
	>>> q
	201
	>>> r
	7
	"""
	return floordiv (n, d), mod(n, d)

q, r = divide_exact(2018, 10)
print(q)
print(r)