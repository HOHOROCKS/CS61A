def inside(out):
	anger = lambda fear: fear(disgust)
	fear = lambda disgust: anger(out)
	disgust = 3
	return fear(5)

fear, disgust = 2, 4
inside(lambda fear: fear + disgust)


def jazz(hands):
	if hands < out:
		print (hands * 5)
		return hands * 5
	else:
		print (hands)
		return jazz(hands // 2) + 1

def twist(shout, it, out = 7):
	while shout:
		shout, out = it(shout), print(shout, out)
	return lambda out: print(shout, out)

hands, out = 2, 3