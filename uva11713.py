import re


tc = int(input())
for i in range(tc):
    s1 = re.sub(r"[aeiou]", "_", input())
    s2 = re.sub(r"[aeiou]", "_", input())
    print("Yes" if s1 == s2 else "No")
