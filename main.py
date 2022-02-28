from typing import List


WORDS_SOURCE = "/usr/share/dict/words"
MIN_WORD_LEN = 4


def get_input() -> str:
    return input("Enter the puzzle letters, with the central one first:")


def read_words() -> List[str]:
    words: List[str] = []
    with open(WORDS_SOURCE) as f:
        lines = f.readlines()

    for word in lines:
        stripped_word = word.strip()
        if len(stripped_word) >= MIN_WORD_LEN:
            words.append(stripped_word.upper())

    return words


def consider_word(word: str , inp: str) -> None:
    if inp[0] not in word:
        return
    for letter in word:
        if letter not in inp:
            return

    print(word)


def helper():
    inp = ""
    while len(inp) != 7:
        inp = get_input().upper()

    words = sorted(read_words())
    for word in words:
        consider_word(word, inp)


if __name__ == '__main__':
    helper()

