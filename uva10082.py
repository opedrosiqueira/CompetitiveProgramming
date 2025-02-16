import sys

def getCorrect(c):
    if c == '1': return '`'
    if c == '2': return '1'
    if c == '3': return '2'
    if c == '4': return '3'
    if c == '5': return '4'
    if c == '6': return '5'
    if c == '7': return '6'
    if c == '8': return '7'
    if c == '9': return '8'
    if c == '0': return '9'
    if c == '-': return '0'
    if c == '=': return '-'
    if c == 'W': return 'Q'
    if c == 'E': return 'W'
    if c == 'R': return 'E'
    if c == 'T': return 'R'
    if c == 'Y': return 'T'
    if c == 'U': return 'Y'
    if c == 'I': return 'U'
    if c == 'O': return 'I'
    if c == 'P': return 'O'
    if c == '[': return 'P'
    if c == ']': return '['
    if c == '\\': return ']'
    if c == 'S': return 'A'
    if c == 'D': return 'S'
    if c == 'F': return 'D'
    if c == 'G': return 'F'
    if c == 'H': return 'G'
    if c == 'J': return 'H'
    if c == 'K': return 'J'
    if c == 'L': return 'K'
    if c == ';': return 'L'
    if c == '\'': return ';'
    if c == 'X': return 'Z'
    if c == 'C': return 'X'
    if c == 'V': return 'C'
    if c == 'B': return 'V'
    if c == 'N': return 'B'
    if c == 'M': return 'N'
    if c == ',': return 'M'
    if c == '.': return ','
    if c == '/': return '.'
    return c


for line in sys.stdin:
    for c in line:
        print(getCorrect(c), end="")
