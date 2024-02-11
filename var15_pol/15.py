def f(x, a):
    return (x % 12 == 0) and (70 <= x <= 80) and not (x % a == 0)


counter = 0
for a in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if f(x, a):
            flag = False
            break
    if flag:
        counter += 1
        print(a)

print("counter =", counter)
