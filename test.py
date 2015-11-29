import fhack
import random

def compareLikeness(word, other):
	likeness = 0

	for i in range(0, len(word)):
		if word[i] == other[i]:
			likeness += 1

	return likeness

if __name__ == "__main__":
	txt = open("tests.txt")
	lines = txt.readlines()

	for line in lines:
		words = line.strip().split(" ")
		target = random.choice(words).upper()

		hack = fhack.FalloutHacker(words)
		tries = 0
		word = ""

		while word != target and hack.hasWords():
			word = hack.suggestWord()
			tries += 1
			likeness = compareLikeness(target, word)
			hack.eliminateWord(word, likeness)

		if word == target:
			print "Guessed " + target + " after " + str(tries) + " attempts"
		else:
			print "Unable to find " + target
