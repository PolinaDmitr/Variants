f = [0] * 23024
f[0] = 5
f[1] = 5
f[2] = 5

for i in range(2, 23024):
    f[i] = f[i - 2] + i
print(f[23023])