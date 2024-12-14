from sys import stdin

for tc, line in enumerate(stdin, start=1):

    sequencenumber = 0
    sequences = [sequencenumber]
    for i in range(1, len(line)):
        if line[i] != line[i - 1]:
            sequencenumber += 1
        sequences.append(sequencenumber)

    print(f"Case {tc}:")
    qn = int(input())
    for _ in range(qn):
        i, j = list(map(int, input().split()))
        print("Yes" if sequences[i] == sequences[j] else "No")
