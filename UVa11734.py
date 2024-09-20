n = int(input())
for i in range(1, n + 1):
    team = input()
    judge = input()
    if team == judge:
        print(f"Case {i}: Yes")
    elif team.replace(" ", "") == judge:
        print(f"Case {i}: Output Format Error")
    else:
        print(f"Case {i}: Wrong Answer")
