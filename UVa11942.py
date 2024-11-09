tc = int(input())
print("Lumberjacks:")
for i in range(tc):
    lumberjacks = input().split()

    asc = True
    for j in range(9):  # testa ordem crescente
        if int(lumberjacks[j]) > int(lumberjacks[j + 1]):
            asc=False
            break

    desc=True
    for j in range(9):  # testa ordem decrescente
        if int(lumberjacks[j]) < int(lumberjacks[j + 1]):
            desc=False
            break
    print("Ordered" if asc or desc else "Unordered")
