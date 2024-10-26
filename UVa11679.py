b, n = map(int, input.split())

banks = list(map(int, input.split()))

for _ in range(n):
    d, c, v = map(int, input.split())
    banks[d - 1] -= v
    banks[c - 1] += v
