
def product(seq: list[int]) -> int:
    result = 1
    for item in seq:
        result *= item
    return result
