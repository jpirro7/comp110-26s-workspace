"""Dictionary Utility Functions."""

__author__ = "730871026"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary with keys and values inverted."""
    result: dict[str, str] = {}

    for key in input:
        value: str = input[key]
        if value in result:
            raise KeyError("Duplicate key when inverting dictionary.")
        result[value] = key

    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Return the most frequently occurring color."""
    color_counts: dict[str, int] = {}

    for name in favorites:
        color: str = favorites[name]

        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_common: str = ""
    highest_count: int = 0

    for color in color_counts:
        if color_counts[color] > highest_count:
            most_common = color
            highest_count = color_counts[color]

    return most_common


def count(values: list[str]) -> dict[str, int]:
    """Return a dictionary counting occurrences of each value."""
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words into lists by their starting letter."""
    result: dict[str, list[str]] = {}

    for word in words:
        if word.isalpha():
            first_letter: str = word[0].lower()

            if first_letter in result:
                result[first_letter].append(word)
            else:
                result[first_letter] = [word]

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Mutate attendance dictionary by adding a student to a day's list."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
