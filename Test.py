names = ["Jennifer", "Albatross", "Justin", "Dave", "Shankarnarayan", "Ezra", "Alice", "Kwabena"]

x = 0

while x < len(names):
    names_equal_or_less = []

    y = 0
    while y < len(names):
        if names[x] == names[y]:
            pass

        elif len(names[y]) <= len(names[x]):
            names_equal_or_less.append(names[y])

        y += 1

    print(f"Names shorter than or equal to {names[x]}: {names_equal_or_less}")
    x += 1