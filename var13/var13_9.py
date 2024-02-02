import os
# для собирания путей в операционке
from math import prod


counter = 0
# чтобы не заморачиваться, можно расположить файл не в папке
# for x in open('9.txt')
for x in open(os.path.join('resource', '9.txt')):
    line = list(map(int, x.split()))
    list_repeat = [x for x in line if line.count(x) == 2]
    list_alone = []
    for y in line:
        if line.count(y) == 1:
            list_alone.append(y)
    if len(list_repeat) == 4 and len(list_alone) == 3:
        if prod(list_repeat) > prod(list_alone) * 2:
            counter += 1

print(counter)
