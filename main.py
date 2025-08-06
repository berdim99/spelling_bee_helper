import sys
from typing import List


WORDS_SOURCE = "/usr/share/dict/words"
MIN_WORD_LEN = 4


def read_words() -> List[str]:
    words: Set[str] = set()
    with open(WORDS_SOURCE) as f:
        lines = f.readlines()

    for word in lines:
        stripped_word = word.strip()
        if len(stripped_word) >= MIN_WORD_LEN:
            w = stripped_word.upper()
            words.add(w)

    return list(words)


def consider_word(word: str , inp: str) -> None:
    if inp[0] not in word:
        return
    for letter in word:
        if letter not in inp:
            return

    print(word)


def helper():
    if len(sys.argv) != 2:
        print("Usage: python main.py <puzzle_letters>")
        print("Example: python main.py ABCDEFG")
        sys.exit(1)
    
    inp = sys.argv[1].upper()
    if len(inp) != 7:
        print("Error: Puzzle letters must be exactly 7 characters long")
        sys.exit(1)

    words = sorted(read_words())
    for word in words:
        consider_word(word, inp)


if __name__ == '__main__':
    helper()

