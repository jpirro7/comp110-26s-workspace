"""Use sub-functions to create one large function for information about a tea party."""

__author__: str = "730871026"


def main_planner(guests: int) -> None:
    """Entry point of the tea party planning program."""
    # Unsure at first whether this function should return a value or just print output.
    print("A Cozy Tea Party for", guests, "People")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Total Cost:",
        cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)),
    )


def tea_bags(people: int) -> int:
    """Compute the number of tea bags needed for a tea party."""
    return people * 2


def treats(people: int) -> int:
    """Compute the number of treats needed for a tea party."""
    # Had to remember to use a keyword argument when calling tea_bags.
    teas = tea_bags(people=people)
    # Needed to explicitly convert to int here to avoid a type mismatch.
    return int(teas * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the total cost of tea bags and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
