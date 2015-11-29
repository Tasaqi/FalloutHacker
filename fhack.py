import random

class FalloutHacker:
	"""Hacker for the terminals in Fallout"""

	def __init__(self, words):
		"""Creates the hacker with a specified list of words."""
		self.all_words = map(lambda x: x.upper(), filter(lambda x: x, words))
		self.reset()

	def compareLikeness(self, word, other):
		"""Compare the likeness of two words"""
		likeness = 0
		for i in range(0, len(word)):
			if word[i] == other[i]:
				likeness += 1
		return likeness

	def eliminateWord(self, word, likeness):
		"""Eliminate a word from the list of possible words"""
		self.possible_words.remove(word)
		self.attempted_words.append((word, likeness))

	def hasWords(self):
		"""Checks if the hacker has possible words"""
		return len(self.possible_words) != 0

	def reset(self):
		"""Resets the hack, allowing you to try again (if the input was wrong or anything)"""
		self.possible_words = list(self.all_words)
		self.attempted_words = list()

	def suggestWord(self):
		"""Suggest one of the words from the list of possible words"""
		suggestions = list()

		if len(self.attempted_words) != 0:
			for word in self.possible_words:
				similarity = 0
				for attempted in self.attempted_words:
					likeness = self.compareLikeness(word, attempted[0])
					if likeness > 0 and attempted[1] == 0:
						similarity -= 1
					elif likeness >= attempted[1]:
						similarity += 1
				suggestions.append((word, similarity))

		if len(suggestions) != 0:
			suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
			return suggestions[0][0]
		else:
			return random.choice(self.possible_words)


# Running the script directly

if __name__ == "__main__":
	print "Enter all the available words, separated by a spaces:"
	words = raw_input()

	hacker = FalloutHacker(words.split(" "))

	print "Enter the likeness value for the chosen words (leave empty to quit)"
	while hacker.hasWords():
		choice = hacker.suggestWord()
		likeness = raw_input(choice + ": ")

		if likeness == "":
			break # lol we done

		likeness = int(likeness)
		hacker.eliminateWord(choice, likeness)
