# Fallout Hacker

Python script helping you to hack the terminals in Fallout 4.

![Screenshot](https://raw.githubusercontent.com/michaelenger/FalloutHacker/master/screenshot.png)

## Usage

### As a standalone script

Run the `fhack.py` script and it will ask for the list of words. Then it will suggest words to try and you have to specify the likeness value for the suggested words. As you do this it will eliminate the words that don't fit and give you new suggestions.

```shell
python fhack.py
```

You can also specify the words as parameters when running the script:

```shell
python fhack.py test ones twos thrs
```

### As a module

If you import the `fhack` module you can use the `FalloutHacker` class directly.

```python
from fhack import FalloutHacker

words = ["test", "ones", "twos", "thrs"]

hacker = FalloutHacker(words)
```

The main methods to use are `suggest_word` and `eliminate_word` which give you a suggestion to try and eliminate that word from the possible suggestions respectively.

```python
word = hacker.suggest_word()
likeness = input("What is the likeness of the word: " + word + "? ")
hacker.eliminate_word(word, likeness)
```

Eliminating words (and specifying the likeness) will improve your chances to get the correct word on the next suggestion.

Another, simpler, way to use the class is the `next` method, which combines getting the next word and eliminating words in one go.

```python
word = hacker.next() # Just get a word without eliminating anything
word = hacker.next(2) # Eliminate the previous word with a likeness of 2
if word != None: # The word will be None if there are no words left
```

You can use `has_words` to check if there are any suggestions left and `reset` to remove all eliminations and return to the initial state.

## Testing

You can test the script by running the `test.py` script.

```shell
python test.py
```
