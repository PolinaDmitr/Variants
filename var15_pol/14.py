import string
from string import digits, ascii_lowercase


for x in (digits + ascii_lowercase)[:17]:
    left = int(f'12346{x}17', 17)
    right = int(f'7{x}171', 17)
    if (left + right) % 16 == 0:
        print(x, (left + right) // 16)
