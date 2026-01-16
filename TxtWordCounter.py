def count_words(file: str) -> int:
    with open(file, "r") as f:
        content = f.read()
    words = 0
    inword = False
    for char in content:
        if char.isspace():
            inword = False
            continue
        elif not inword:
            words += 1
            inword = True
    return words

print(count_words("test.txt"))