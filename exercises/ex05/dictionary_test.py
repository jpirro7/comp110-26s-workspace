"""Unit tests for dictionary utility functions."""

__author__ = "730871026"

import pytest

from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


# invert tests


def test_invert_basic() -> None:
    """Use case: simple key/value inversion."""
    assert invert({"a": "x", "b": "y"}) == {"x": "a", "y": "b"}


def test_invert_single_pair() -> None:
    """Use case: dictionary with one pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_keyerror() -> None:
    """Edge case: duplicate values should raise KeyError."""
    with pytest.raises(KeyError):
        invert({"a": "x", "b": "x"})


# favorite_color tests


def test_favorite_color_basic() -> None:
    """Use case: clear most frequent color."""
    data = {"A": "blue", "B": "red", "C": "blue"}
    assert favorite_color(data) == "blue"


def test_favorite_color_tie() -> None:
    """Use case: tie returns first encountered color."""
    data = {"A": "blue", "B": "red"}
    assert favorite_color(data) == "blue"


def test_favorite_color_single() -> None:
    """Edge case: single entry dictionary."""
    data = {"A": "green"}
    assert favorite_color(data) == "green"


# count tests


def test_count_basic() -> None:
    """Use case: multiple repeated values."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_all_unique() -> None:
    """Use case: all unique values."""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_empty() -> None:
    """Edge case: empty list."""
    assert count([]) == {}


# alphabetizer tests


def test_alphabetizer_basic() -> None:
    """Use case: grouping by first letter."""
    result = alphabetizer(["apple", "banana", "apricot"])
    assert result == {"a": ["apple", "apricot"], "b": ["banana"]}


def test_alphabetizer_case() -> None:
    """Use case: handles uppercase letters."""
    result = alphabetizer(["Apple", "banana"])
    assert result == {"a": ["Apple"], "b": ["banana"]}


def test_alphabetizer_empty() -> None:
    """Edge case: empty input list."""
    assert alphabetizer([]) == {}


# update_attendance tests


def test_update_attendance_existing_day() -> None:
    """Use case: add student to existing day."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Bob")
    assert attendance == {"Monday": ["Alice", "Bob"]}


def test_update_attendance_new_day() -> None:
    """Use case: add new day with student."""
    attendance = {}
    update_attendance(attendance, "Tuesday", "Alice")
    assert attendance == {"Tuesday": ["Alice"]}


def test_update_attendance_multiple() -> None:
    """Edge case: multiple updates to same day."""
    attendance = {"Wednesday": []}
    update_attendance(attendance, "Wednesday", "Alice")
    update_attendance(attendance, "Wednesday", "Bob")
    assert attendance == {"Wednesday": ["Alice", "Bob"]}
