def bs(x):
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
    return True


for n in range(51, 100):
    s = '0' + '1' * 100 + '2' * n + '0'
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('012', '30', 1)
        s = s.replace('010', '00', 1)
    res = sum(int(x) for x in s)
    if bs(res):
        print(n)
        break

