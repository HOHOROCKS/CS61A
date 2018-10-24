def longest_increasing_suffix(n):
	m, suffix, k = 10, 0, 1

	while n:
		n, last = n // 10, n % 10
		if last < m:
			m, suffix, k = last, suffix + k * last, 10 * k
		else:
			return suffix
	return suffix

batman, superman, ivy = 1, -2, -3
def nanana(batman):
    while batman(superman) > ivy:
        def batman(joker):
            return ivy
    return -ivy
def joker(superman):
    if superman(batman):
        ivy = -batman
    return nanana
joker(abs)(abs)