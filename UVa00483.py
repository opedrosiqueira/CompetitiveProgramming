from sys import stdin

for line in stdin:
    reversed_words=[]
    for w in line.split():
        reversed_words.append(w[::-1])
    print(" ".join(reversed_words))