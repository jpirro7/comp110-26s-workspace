"""Wordle game implementation for COMP110."""

__author__ = "730871026"
# Emoji constants used to represent guess accuracy
WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(expected_length: int) -> str:
    """Prompt user for a guess of expected_length and return valid guess."""
    # Initial prompt for user input
    guess: str = input(f"Enter a {expected_length} character word: ")
    # Continue prompting until guess lenth = expected length
    while len(guess) != expected_length:
        print(f"That wasn't {expected_length} characters! Try again.")
        guess = input(f"Enter a {expected_length} character word: ")

    return guess


def contains_char(word: str, character: str) -> bool:
    """Return True if character is found anywhere in word, otherwise False."""
    # Ensure the character argument is exactly one character long
    assert len(character) == 1
    index: int = 0
    # Check index of word for a match
    while index < len(word):
        if word[index] == character:
            return True
        index = index + 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Return emoji boxes showing how guess compares to secret."""
    # Ensure guess and secret are the same length
    assert len(guess) == len(secret)

    result: str = ""
    index: int = 0
    # Compare each position of guess to secret
    while index < len(secret):
        if guess[index] == secret[index]:
            result = result + GREEN_BOX
        elif contains_char(secret, guess[index]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX

        index = index + 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns_taken: int = 0
    max_turns: int = len(secret) + 1
    won: bool = False
    # Continue game while turns remain and user has not won
    while turns_taken < max_turns and not won:
        current_turn: int = turns_taken + 1
        print(f"=== Turn {current_turn}/{max_turns} ===")

        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        # Increment turn counter
        turns_taken = turns_taken + 1

    if won:
        print(f"You won in {turns_taken}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
