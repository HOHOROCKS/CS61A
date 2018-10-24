def split(n):
	return n//10, n %10

def luhn_sum(n):
	all_but_last, last = split(n)
	if all_but_last == 0:
		return last
	else:
		return double_luhn_sum(all_but_last) + last

def double_luhn_sum(n):
	all_but_last, last = split(n)
	last *= 2
	if last > 9:
		a, b = split(last)
		last = a + b
		
	if all_but_last == 0:
		return last
	else:
		return luhn_sum(all_but_last) + last