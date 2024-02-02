from itertools import product

counter = 0
for x in product('01234567', repeat = 7):
    s = ''.join(x)
    if x[0] != '0' and sum(y in '0246' for y in x) == 2:
        for y in '135':
            s = s.replace(y, '1')
        if '17' not in s and '71' not in s and '77' not in s:
            counter += 1

print(counter)