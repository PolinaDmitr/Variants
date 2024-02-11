with open("resource\\17-370.txt", "r") as file:
    l = [int(x) for x in file]
    l_max = max(x for x in l if (x < 1000) and
                ((x % 10 + x % 100 // 10 + x // 100) % 10 == 3))
    print(l_max)
    result = []
    for i in range(len(l) - 1):
        a1 = abs(l[i])
        a2 = abs(l[i + 1])
        if ((999 < a1 < 10000 and (a2 < 1000 or a2 > 9999)) or
                (999 < a2 < 10000 and (a1 < 1000 or a1 > 9999))):
            p = a1 * a1 + a2 * a2
            if p % l_max == 0:
                print(a1, a2, p)
                result.append(p)

    print(len(result), max(result))