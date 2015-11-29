import random

print "Enter all the available words, separated by a spaces:"

words = raw_input()
words = map(lambda x: x.upper(), filter(lambda x: x, words.split(" ")))

def determine_likenesses(words, chosen):
	likenesses = []
	for word in words:
		if word != chosen:
			likeness = 0
			for i in range(0, len(word)):
				if word[i] == chosen[i]:
					likeness += 1
			likenesses.append((word, likeness))

	return likenesses

word_found = False

choice = random.choice(words)
while not word_found and len(words):
	words.remove(choice)
	print "Enter the likeness value for the chosen words"
	likeness = int(raw_input(choice + ": "))

	if likeness == 0:
		choice = random.choice(words)
	else:
		likenesses = determine_likenesses(words, choice)
		for pair in likenesses:
			if pair[1] == likeness:
				choice = pair[0]
