with open('resource/17.txt', 'r') as file:
    l = [int(x) for x in file]
    l_max = max(x for x in l if abs(x) % 100 == 50)
    result = []
    for i in range(len(l) - 2):
        if all(9999 < abs(a) < 100000 for a in l[i:i + 3]) \
                and l[i] != l[i + 1] != l[i + 2] != l[i] \
                and l[i] + l[i + 1] + l[i + 2] <= l_max:
            result.append(l[i] + l[i + 1] + l[i + 2])

    print(len(result), max(result))
