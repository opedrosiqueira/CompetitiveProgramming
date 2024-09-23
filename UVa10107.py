import sys

numbers = []
for number in sys.stdin:
    numbers.append(int(number.strip()))
    numbers.sort()
    size = len(numbers)
    median = int(size / 2)
    if size % 2 == 0:
        print(int((numbers[median - 1] + numbers[median]) / 2))
    else:
        print(int(numbers[median]))
