import unittest
import fhack

class TestFalloutHacker(unittest.TestCase):
  def compare(self, word, other):
    likeness = 0
    for i in range(0, len(word)):
      if word[i] == other[i]:
        likeness += 1
    return likeness

  def test_compare(self):
    hack = fhack.FalloutHacker(["TEST"])
    self.assertEqual(hack.compare("TEST", "TEST"), 4)
    self.assertEqual(hack.compare("TEST", "BEST"), 3)
    self.assertEqual(hack.compare("TEST", "NONE"), 0)

  def test_eliminate_word(self):
    hack = fhack.FalloutHacker(["TEST"])
    self.assertTrue(hack.has_words())
    hack.eliminate_word("TEST", 2)
    self.assertFalse(hack.has_words())

  def test_eliminate_word_two_words(self):
    hack = fhack.FalloutHacker(["cat", "hat"])
    hack.eliminate_word("CAT", 2)
    word = hack.suggest_word()
    self.assertEqual(word, "HAT")

  def test_next(self):
    hack = fhack.FalloutHacker(["cat", "hat", "fat"])
    for i in range(3):
      word = hack.next()
      self.assertIn(word, ["CAT", "HAT", "FAT"])
      hack.next(2)
    word = hack.next()
    self.assertIsNone(word)

  def test_has_words(self):
    hack = fhack.FalloutHacker(["TEST"])
    self.assertTrue(hack.has_words())
    hack.eliminate_word("TEST", 2)
    self.assertFalse(hack.has_words())

  def test_reset(self):
    hack = fhack.FalloutHacker(["TEST"])
    self.assertTrue(hack.has_words())
    hack.eliminate_word("TEST", 2)
    self.assertFalse(hack.has_words())
    hack.reset()
    self.assertTrue(hack.has_words())

  def test_suggest_word_single_word(self):
    hack = fhack.FalloutHacker(["Test"])
    word = hack.suggest_word()
    self.assertEqual(word, "TEST")

  def test_suggest_word_multiple_words(self):
    hack = fhack.FalloutHacker(["TEST", "again"])
    word = hack.suggest_word()
    self.assertIn(word, ["TEST", "AGAIN"])

  def test_hack(self):
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
