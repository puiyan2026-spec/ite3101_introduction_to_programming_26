def digit_sum(n: int) -> int:
    total = 0
    for char in str(n):
        total += int(char)
        return total 