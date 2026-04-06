"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730871026"


def input_word() -> str:
    word_input: str = input("Enter a 5-character word: ")
    # I need to check word length but how?
    if len(word_input) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word_input


def input_letter() -> str:
    letter_input: str = input("Enter a single character: ")
    if len(letter_input) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter_input


def contains_char(word: str, letter: str) -> None:
    print("Searching for {letter} in {word}.")
    match_count: int = 0
    # How do I go about checking each index? Use word == letter?
    if word[0] == letter:
        print("{letter} found at index 0.")
        match_count += 1
    if word[1] == letter:
        print("{letter} found at index 1.")
        match_count += 1
    if word[2] == letter:
        print("{letter} found at index 2.")
        match_count += 1
    if word[3] == letter:
        print("{letter} found at index 3.")
        match_count += 1
    if word[4] == letter:
        print("{letter} found at index 4.")
        match_count += 1

    if match_count == 0:
        print("No instances of {letter} found in {word}.")
    elif match_count == 1:
        print("1 instance of {letter} found in {word}.")
    else:
        print("{match_count} instances of {letter} found in {word}.")


def main() -> None:
    # now I need to use the function that will run the game
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()  # this starts my program
