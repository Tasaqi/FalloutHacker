import random
import sys

class FalloutHacker:
  """Hacker for the terminals in Fallout"""

  def __init__(self, words):
    """Creates the hacker with a specified list of words."""
    self.all_words = list(map(lambda x: x.upper(), filter(lambda x: x, words)))
    self.current_word = None
    self.reset()

  def compare(self, word, other):
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

  def next(self, likeness=None):
    """Gets the next word (or None) if there are no more words"""
    if likeness != None and self.current_word != None:
      self.eliminate_word(self.current_word, likeness)
    return self.suggest_word() if self.has_words() else None

  def reset(self):
    """Resets the hack, allowing you to try again (if the input was wrong or anything)"""
    self.possible_words = self.all_words.copy()
    self.attempted_words = list()

  def suggest_word(self):
    """Suggest one of the words from the list of possible words"""
    suggestions = list()

    if len(self.attempted_words) != 0:
      for word in self.possible_words:
        similarity = 0
        for attempted in self.attempted_words:
          likeness = self.compare(word, attempted[0])
          if likeness > 0 and attempted[1] == 0:
            similarity -= 1
          elif likeness >= attempted[1]:
            similarity += 1
        suggestions.append((word, similarity))

    suggestion = None
    if len(suggestions) != 0:
      suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
      suggestion = suggestions[0][0]
    else:
      suggestion = random.choice(self.possible_words)

    self.current_word = suggestion
    return suggestion


# Running the script directly

def main():
  if len(sys.argv) > 1:
    words = sys.argv[1:]
  else:
    print("Enter all the available words, separated by a spaces:")
    words = input().split(" ")

  hacker = FalloutHacker(words)

  print("Enter the likeness value for the chosen words (leave empty to quit)")
  while hacker.has_words():
    choice = hacker.suggest_word()
    likeness = input(choice + ": ")

    if likeness == "":
      break # lol we done

    likeness = int(likeness)
    hacker.eliminate_word(choice, likeness)

if __name__ == "__main__":
  main()
