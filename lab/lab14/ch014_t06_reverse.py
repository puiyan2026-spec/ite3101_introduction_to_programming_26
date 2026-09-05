def reverse(text: str) -> str:
    word = ""
    i = len(text)-1
    while i >= 0:
        word += text[i]
        i -= 1
    return word
