from collections import Counter
from sys import stdin

lines = stdin.readlines()
for i in range(1, len(lines), 2):
    a = Counter(lines[i - 1][:-1])
    b = Counter(lines[i][:-1])
    x = []
    for c in a:
        if c in b:
            x.append(c * min(a[c], b[c]))
    print("".join(sorted(x)))
