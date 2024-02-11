from itertools import product


counter = 0
for n in product('0123', repeat=4):
    if n[0] != '0' and any(n.count(y) > 1 for y in n):
        counter += 1
print(counter)