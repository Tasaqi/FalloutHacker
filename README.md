# Fallout Hacker

Python script helping you to hack the terminals in Fallout 4.

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
import fhack

words = ["test", "ones", "twos", "thrs"]

hacker = fhack.FalloutHacker(words)
```

The main methods to use are `suggestWord` and `eliminateWord` which give you a suggestion to try and eliminate that word from the possible suggestions respectively.

```python
word = hacker.suggestWord()
likeness = input("What is the likeness of the word: " + word + "? ")
hacker.eliminateWord(word, likeness)
```

Eliminating words (and specifying the likeness) will improve your chances to get the correct word on the next suggestion.

## Testing

You can test the script by running the `test.py` script which will read the `tests.txt` file and try to guess a random target word by process of elimination.

```shell
python test.py
```
