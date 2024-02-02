def f12(x):
    alpha = '0123456789AB'
    result = ''
    while x > 0:
        result = alpha[x % 12] + result
        x //= 12
    return result


n_min = 10000
for n in range(1, 10000):
    n12 = f12(n)
    if n % 4 == 0:
        n12 = '2' + n12 + '64'
    else:
        n12 += max(n12)
    n10 = int(n12, 12)
    if 1799 < n10 < n_min:
        n_min = n10
print(n_min)