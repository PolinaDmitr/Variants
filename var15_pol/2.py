def f(x, y, z, w):
    return not (x <= w) or (y <= z) or not y


print("x y z w")
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                result = f(x, y, z, w)
                if not result:
                    print(x, y, z, w, '=', result)
# xwyz