import random

class FalloutHacker:
	"""Hacker for the terminals in Fallout"""

	def __init__(self, words):
		"""Creates the hacker with a specified list of words."""
		self.all_words = map(lambda x: x.upper(), filter(lambda x: x, words))
		self.reset()

	def compare_likeness(self, word, other):
		"""Compare the likeness of two words"""
		likeness = 0
		for i in range(0, len(word)):
			if word[i] == other[i]:
				likeness += 1
		return likeness

	def eliminate_word(self, word, likeness):
		"""Eliminate a word from the list of possible words"""
		self.possible_words.remove(word)
		self.attempted_words.append((word, likeness))

	def has_words(self):
		"""Checks if the hacker has possible words"""
		return len(self.possible_words) != 0

	def reset(self):
		"""Resets the hack, allowing you to try again (if the input was wrong or anything)"""
		self.possible_words = list(self.all_words)
		self.attempted_words = list()

	def suggest_word(self):
		"""Suggest one of the words from the list of possible words"""
		if len(self.attempted_words) != 0:
			like_words = list()
			for word in self.possible_words:
				likeness = 0
				for attempted in self.attempted_words:
					likeness += self.compare_likeness(word, attempted[0])
				like_words.append((word, likeness))
			like_words = sorted(like_words, key=lambda x: x[1], reverse=True)
			return like_words[0][0]
		else:
			return random.choice(self.possible_words)

# Running the script directly

if __name__ == "__main__":
	print "Enter all the available words, separated by a spaces:"
	words = raw_input()

	hacker = FalloutHacker(words.split(" "))

	print "Enter the likeness value for the chosen words (leave empty to quit)"
	while hacker.has_words():
		choice = hacker.suggest_word()
		likeness = raw_input(choice + ": ")

		if likeness == "":
			break # lol we done

		likeness = int(likeness)
		hacker.eliminate_word(choice, likeness)
