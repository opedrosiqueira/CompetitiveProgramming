# não consegui resolver, deu time limit exceded. tentei usando tanto dicionário quanto endereçamento direto, e por incrível que pareca, medindo tempo com -m cProfile, endereçamento direto é pior que dicionário, por conta da chamada à função ord() (???). esse artigo fala sobre a entrada ser iso8859-1 e muito grande pra usar um simples input() ou print: https://www.redgreencode.com/solving-uva-11340-in-java/. o udebug diz que apenas nos artigos há caracteres binários, na tabela não há. as seguintes alternativas foram testadas, usando o 01-profiler.py, da mais rápida pra mais devagar:


def alternativa1():
    import io
    from sys import stdin, stdout

    input_stream = io.TextIOWrapper(stdin.buffer, encoding="iso-8859-1")
    read = input_stream.readline
    write = stdout.write

    n = int(read())

    for _ in range(n):
        char_values = {}
        k = int(read())

        for _ in range(k):
            char, value = read().split()
            char_values[char] = int(value)

        m = int(read())
        total_payment = 0

        for _ in range(m):
            article_line = read()
            for char in article_line:
                if char in char_values:
                    total_payment += char_values[char]

        write(f"{(total_payment / 100):.2f}$\n")


def alternativa2():
    n = int(input())

    for _ in range(n):
        char_values = {}
        k = int(input())

        for _ in range(k):
            char, value = input().split()
            char_values[char] = int(value)

        m = int(input())
        total_payment = 0

        for _ in range(m):
            article_line = input()
            for char in article_line:
                if char in char_values:
                    total_payment += char_values[char]

        print(f"{(total_payment / 100):.2f}$")


def alternativa3():
    import io
    from sys import stdin, stdout

    input_stream = io.TextIOWrapper(stdin.buffer, encoding="iso-8859-1")
    outputs = []

    data = input_stream.read().split("\n")
    index = -1

    def read():
        nonlocal index
        index += 1
        return data[index]

    n = int(read())

    for _ in range(n):
        char_values = {}
        k = int(read())

        for _ in range(k):
            char, value = read().split()
            char_values[char] = int(value)

        m = int(read())
        total_payment = 0

        for _ in range(m):
            article_line = read()
            for char in article_line:
                if char in char_values:
                    total_payment += char_values[char]

        outputs.append(f"{(total_payment / 100):.2f}$")

    stdout.write("\n".join(outputs))


def alternativa4():
    import sys

    inputs = sys.stdin.read().splitlines()
    current = 0
    outputs = []

    n = int(inputs[current])
    current += 1

    for _ in range(n):
        char_values = {}
        k = int(inputs[current])
        current += 1
        for _ in range(k):
            char, value = inputs[current].split()
            current += 1
            char_values[char] = int(value)

        m = int(inputs[current])
        current += 1
        total_payment = 0

        for _ in range(m):
            article_line = inputs[current]
            current += 1
            for char in article_line:
                if char in char_values:
                    total_payment += char_values[char]

        outputs.append(f"{(total_payment / 100):.2f}$")

    sys.stdout.write("\n".join(outputs))


def alternativa5():
    from collections import defaultdict
    import io
    from sys import stdin, stdout

    input_stream = io.TextIOWrapper(stdin.buffer, encoding="iso-8859-1")
    read = input_stream.readline
    write = stdout.write

    n = int(read())

    for _ in range(n):
        char_values = defaultdict(int)
        k = int(read())

        for _ in range(k):
            char, value = read().split()
            char_values[char] = int(value)

        m = int(read())
        total_payment = 0

        for _ in range(m):
            article_line = read()
            for char in article_line:
                total_payment += char_values[char]

        write(f"{(total_payment / 100):.2f}$\n")


def alternativa6():
    import io
    from sys import stdin, stdout

    input_stream = io.TextIOWrapper(stdin.buffer, encoding="iso-8859-1")
    read = input_stream.readline
    write = stdout.write

    n = int(read())

    for _ in range(n):
        char_values = [0] * 511  # `[0] * size` eh mais rapido que `[0 for _ in range(size)]`

        k = int(read())

        for _ in range(k):
            char, value = read().split()
            char_values[ord(char)] = int(value)

        m = int(read())
        total_payment = 0

        for _ in range(m):
            article_line = read()
            for char in article_line:
                total_payment += char_values[ord(char)]

        write(f"{(total_payment / 100):.2f}$\n")


def alternativa7():
    import io
    from sys import stdin, stdout

    input_stream = io.TextIOWrapper(stdin.buffer, encoding="iso-8859-1")
    read = input_stream.readline
    write = stdout.write

    ascii_lookup = {chr(i): i for i in range(128)}  # Precomputed ASCII values

    n = int(read())

    for _ in range(n):
        char_values = [0] * 511  # `[0] * size` eh mais rapido que `[0 for _ in range(size)]`

        k = int(read())

        for _ in range(k):
            char, value = read().split()
            char_values[ascii_lookup.get(char, 0)] = int(value)

        m = int(read())
        total_payment = 0

        for _ in range(m):
            article_line = read()
            for char in article_line:
                total_payment += char_values[ascii_lookup.get(char, 0)]

        write(f"{(total_payment / 100):.2f}$\n")


def alternativa8():
    import io
    from sys import stdin, stdout

    def getcode(c):
        if c == " ":
            return 32
        if c == "!":
            return 33
        if c == '"':
            return 34
        if c == "#":
            return 35
        if c == "$":
            return 36
        if c == "%":
            return 37
        if c == "&":
            return 38
        if c == "'":
            return 39
        if c == "(":
            return 40
        if c == ")":
            return 41
        if c == "*":
            return 42
        if c == "+":
            return 43
        if c == ",":
            return 44
        if c == "-":
            return 45
        if c == ".":
            return 46
        if c == "/":
            return 47
        if c == "0":
            return 48
        if c == "1":
            return 49
        if c == "2":
            return 50
        if c == "3":
            return 51
        if c == "4":
            return 52
        if c == "5":
            return 53
        if c == "6":
            return 54
        if c == "7":
            return 55
        if c == "8":
            return 56
        if c == "9":
            return 57
        if c == ":":
            return 58
        if c == ";":
            return 59
        if c == "<":
            return 60
        if c == "=":
            return 61
        if c == ">":
            return 62
        if c == "?":
            return 63
        if c == "@":
            return 64
        if c == "A":
            return 65
        if c == "B":
            return 66
        if c == "C":
            return 67
        if c == "D":
            return 68
        if c == "E":
            return 69
        if c == "F":
            return 70
        if c == "G":
            return 71
        if c == "H":
            return 72
        if c == "I":
            return 73
        if c == "J":
            return 74
        if c == "K":
            return 75
        if c == "L":
            return 76
        if c == "M":
            return 77
        if c == "N":
            return 78
        if c == "O":
            return 79
        if c == "P":
            return 80
        if c == "Q":
            return 81
        if c == "R":
            return 82
        if c == "S":
            return 83
        if c == "T":
            return 84
        if c == "U":
            return 85
        if c == "V":
            return 86
        if c == "W":
            return 87
        if c == "X":
            return 88
        if c == "Y":
            return 89
        if c == "Z":
            return 90
        if c == "[":
            return 91
        if c == "\\":
            return 92
        if c == "]":
            return 93
        if c == "^":
            return 94
        if c == "_":
            return 95
        if c == "`":
            return 96
        if c == "a":
            return 97
        if c == "b":
            return 98
        if c == "c":
            return 99
        if c == "d":
            return 100
        if c == "e":
            return 101
        if c == "f":
            return 102
        if c == "g":
            return 103
        if c == "h":
            return 104
        if c == "i":
            return 105
        if c == "j":
            return 106
        if c == "k":
            return 107
        if c == "l":
            return 108
        if c == "m":
            return 109
        if c == "n":
            return 110
        if c == "o":
            return 111
        if c == "p":
            return 112
        if c == "q":
            return 113
        if c == "r":
            return 114
        if c == "s":
            return 115
        if c == "t":
            return 116
        if c == "u":
            return 117
        if c == "v":
            return 118
        if c == "w":
            return 119
        if c == "x":
            return 120
        if c == "y":
            return 121
        if c == "z":
            return 122
        if c == "{":
            return 123
        if c == "|":
            return 124
        if c == "}":
            return 125
        if c == "~":
            return 126
        return 0

    input_stream = io.TextIOWrapper(stdin.buffer, encoding="iso-8859-1")
    read = input_stream.readline
    write = stdout.write

    n = int(read())

    for _ in range(n):
        char_values = [0] * 511  # `[0] * size` eh mais rapido que `[0 for _ in range(size)]`

        k = int(read())

        for _ in range(k):
            char, value = read().split()
            char_values[getcode(char)] = int(value)

        m = int(read())
        total_payment = 0

        for _ in range(m):
            article_line = read()
            for char in article_line:
                total_payment += char_values[getcode(char)]

        write(f"{(total_payment / 100):.2f}$\n")


if __name__ == "__main__":
    alternativa7()
