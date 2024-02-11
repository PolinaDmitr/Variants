with open("resource\\9-210.csv", "r") as file:
    counter = 0
    for line in file:
        value = [int(x) for x in line.split(';')]
        max_line = max(value)
        min_line = min(value)
        if (value.count(max_line) == 1 and
                any(value.count(x) > 1 for x in value if x != max_line) and
                (max_line + min_line) * 2 > sum(value)):
            counter += 1

    print(counter)

