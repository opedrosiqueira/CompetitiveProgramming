t = int(input())
for i in range(1, t + 1):
    n = int(input())
    mile = juice = 0
    for s in input().split():
        s = int(s)
        mile += 10 + s // 30 * 10
        juice += 15 + s // 60 * 15
    if mile < juice:
        print(f"Case {i}: Mile {mile}")
    elif juice < mile:
        print(f"Case {i}: Juice {juice}")
    else:
        print(f"Case {i}: Mile Juice {mile}")
