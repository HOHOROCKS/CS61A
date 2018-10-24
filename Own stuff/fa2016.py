def repeat(f, x, n):
	total, k = 0, 0
	while k <= n:
		total = total + x
		x = f(x)
		k += 1
	return total

def sum(n):
	f = lambda x: pow(n , 2)
	return repeat(f, 0, n)

def confirmer(code):
	def confirm1(d, t):
		def result(digit):
			if d == digit:
				return t
			else:
				return False
		return result

	def extend(prefix, rest):
		left, last = prefix // 10, prefix % 10

		if prefix < 10:
			return confirm1 (prefix, rest)
		else:
			return extend(left, confirm1(last, rest))
	return extend(code, True)

def decode(f, y = 0):
	d = 0
	while d < 10:
		x, code = f(d), y * 10 + d
		if x == True:
			return code
		elif x == False:
			d += 1
		else:
			return decode(x, y = code)