def grades_variance(grades_input: List[float]) -> float:
    avg = grades_average(grades_input)
    total = 0
    for grade in grades_input:
        total += (grade - avg) ** 2
    return total / len(grades_input)

print(grades_variance(grades))