def square(x):
	return x * x

def make_adder(n):
	def adder(k):
		return n + k
	return adder

def compose(f, g):
	def h(x):
		return f(g(x))
	return h

def decompose1(f, h):
	def g(x):
		def r(y):
			if f(y) == h(x):
				return y
			else:
				print(y)
				return r(y+1)
		return r(0)
	return g

def add_one(x):
	return x + 1

def square_then_add_one(x):
	return x * x + 1

