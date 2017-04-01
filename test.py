import unittest
import fhack

class TestFalloutHacker(unittest.TestCase):
  def compare(self, word, other):
    likeness = 0
    for i in range(0, len(word)):
      if word[i] == other[i]:
        likeness += 1
    return likeness

  def test_single_word(self):
    hack = fhack.FalloutHacker(["Test"])
    word = hack.suggest_word()
    self.assertEqual(word, "TEST")

  def test_multiple_words(self):
    hack = fhack.FalloutHacker(["TEST", "again"])
    word = hack.suggest_word()
    self.assertIn(word, ["TEST", "AGAIN"])

  def test_suggest_simple_word(self):
    hack = fhack.FalloutHacker(["cat", "fat", "hat"])
    target = "CAT"
    word = ""
    while word != target and hack.has_words():
      word = hack.suggest_word()
      if word != target:
        hack.eliminate_word(word, 2)
    self.assertEqual(word, target)

  def test_suggest_complex_word(self):
    hack = fhack.FalloutHacker([
        "dancing", "talking", "walking", "command", "pattern", "history",
        "milling", "torture", "warrior", "sealant", "tyranny", "cousins"
    ])
    target = "WARRIOR"
    word = ""
    while word != target and hack.has_words():
      word = hack.suggest_word()
      if word != target:
        hack.eliminate_word(word, self.compare(word, target))
    self.assertEqual(word, target)

if __name__ == "__main__":
  unittest.main()
