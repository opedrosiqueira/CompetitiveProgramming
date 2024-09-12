import re

number = input().strip()
while number != "*":
    if re.fullmatch(r"[-+]?\d+((\.\d+)|((\.\d+)?e[-+]?\d+))", number, re.IGNORECASE):
        print(number, "is legal.")
    else:
        print(number, "is illegal.")
    number = input().strip()
