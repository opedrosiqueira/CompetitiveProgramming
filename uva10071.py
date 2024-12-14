from sys import stdin

for line in stdin:
    v, t = list(map(int, line.split()))
    print(2 * v * t)
