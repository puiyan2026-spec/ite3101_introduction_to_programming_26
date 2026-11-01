from typing import List

# Sample grades list
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input: List[float]):
    """
    Print each grade in the list.
    """
    for grade in grades_input:
        print(grade)


def grades_sum(scores: List[float]) -> float:
    """
    Computes the sum of all grades in the list.
    """
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input: List[float]) -> float:
    """
    Computes the average of all grades in the list.
    """
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / len(grades_input)
    return average


def grades_variance(scores: List[float]) -> float:
    """
    Computes the variance of the grades in the list.
    """
    average = grades_average(scores)
    variance = sum((average - score) ** 2 for score in scores) / len(scores)
    return variance


# This ensures compatibility with the `execfile` function in the test
if __name__ == "__main__":
    # Print only the variance value, as required by the test
    print(grades_variance(grades))