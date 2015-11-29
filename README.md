# Fallout Hacker

Python script allowing you to hack the terminals in Fallout.

## Usage

Run the `fhack.py` script and it will ask for the list of words. Then it will suggest words to try and you have to specify the likeness value for the suggested words. As you do this it will eliminate the words that don't fit and give you new suggestions.

```shell
python fhack.py
```

## Testing

You can test the script by running hte `test.py` script which will read the `tests.txt` file and try to guess a random target word by process of elimination.

```shell
python test.py
```
