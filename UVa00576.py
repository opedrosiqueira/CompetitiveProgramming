import re

haiku = input()
while haiku != "e/o/i":
    haiku = haiku.split("/")
    if len(re.findall(r"[aeiouy]+", haiku[0])) != 5:
        print(1)
    elif len(re.findall(r"[aeiouy]+", haiku[1])) != 7:
        print(2)
    elif len(re.findall(r"[aeiouy]+", haiku[2])) != 5:
        print(3)
    else:
        print("Y")
    haiku = input()
