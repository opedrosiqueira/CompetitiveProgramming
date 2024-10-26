b, n = map(int, input().split())

while b != 0 or n != 0:
    banks = list(map(int, input().split()))

    for _ in range(n):
        d, c, v = map(int, input().split())
        banks[d - 1] -= v
        banks[c - 1] += v

    success = True
    for bank in banks:
        if bank < 0:
            success = False
            break

    print("S" if success else "N")

    b, n = map(int, input().split())
