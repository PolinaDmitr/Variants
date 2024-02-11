def three(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s


max_n = 0
for n in range(1000):
    n3 = three(n)
    if sum(int(i) for i in n3) % 3 == 0:
        n3 = '20' + n3
    else:
        n3 = '10' + n3

    r = int(n3, 3)
    if r < 100 and n > max_n:
        max_n = n

print(max_n)