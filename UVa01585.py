n = int(input())
while n > 0:
    test = input()
    total = 0
    current = 1
    for problem in test:
        if problem == "O":
            total += current
            current += 1
        else:
            current = 1
    print(total)
    n -= 1
