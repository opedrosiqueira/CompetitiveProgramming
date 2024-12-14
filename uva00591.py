tc = 1
blocks = int(input())
while blocks != 0:
    stacks = list(map(int, input().split()))
    avg = int(sum(stacks) / len(stacks))
    moves = 0
    for stack in stacks:
        if stack > avg:
            moves += stack - avg
    print(f"Set #{tc}\nThe minimum number of moves is {moves}.\n")
    tc += 1
    blocks = int(input())
