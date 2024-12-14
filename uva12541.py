n = int(input())
youngest = (0, 0, 0, "")
oldest = (9999, 99, 99, "")
while n:
    line = input().split()
    current = (int(line[3]), int(line[2]), int(line[1]), line[0])
    if current < oldest:
        oldest = current
    if current > youngest:
        youngest = current
    n -= 1
print(youngest[3])
print(oldest[3])
