import sys

numbers = []
for number in sys.stdin:
    numbers.append(int(number.strip()))
    numbers.sort()
    size = len(numbers)
    if size % 2 == 0:
        print(int((numbers[int(size / 2) - 1] + numbers[int(size / 2)]) / 2))
    else:
        print(int(numbers[int(size / 2)]))
