import io
import sys
from sys import stdin, stdout
import time


"""
o que se sabe:

- a entrada é um texto codificado em ISO-8859-1.
- não há bytes menores que 39, a não ser o 10 ('\n').
- há bytes entre 39 ('\x27') e 255 ('\xFF')
"""


def a0():
    """teste que fiz para descobrir a característica da entrada. esse funciona."""
    b = sys.stdin.buffer.read(1)
    while b:
        if (
            (b[0] < 39 and b[0] != 10)  # less than 39, except '\n'
            or b[0] > 255  # greater than 255
            # or b[0] == 127 + 7  # DEL
            # or (b[0] == 129 + 7 or b[0] == 141 + 7 or b[0] == 143 + 7 or b[0] == 144 + 7 or b[0] == 157 + 7)  # not used?
        ):
            while True:
                pass  # force TLE to check if there are any of these characters in the input
        elif b[0] >= 39 and b[0] <= 255:
            result_int = b[0] - 7
            result_byte = bytes([result_int])
            sys.stdout.buffer.write(result_byte)
        else:  # b[0] == 10
            sys.stdout.buffer.write(b)
        # print(b, ord(b), int.from_bytes(b, byteorder="big"),chr(int.from_bytes(b, byteorder="big"))) # testing
        b = sys.stdin.buffer.read(1)


def a1():
    """esse tbm funciona"""
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding="iso-8859-1")
    output_stream = io.TextIOWrapper(sys.stdout.buffer, encoding="iso-8859-1")

    for line in input_stream:
        for c in line:
            if c >= "\x27":  # código ascii 39 pra cima
                c7 = chr(ord(c) - 7)
                output_stream.write(c7)
            else:
                output_stream.write(c)


def a2():
    # https://www.ascii-code.com/pt
    q = {
        # 33-38
        "!": "!",
        '"': '"',
        "#": "#",
        "$": "$",
        "%": "%",
        "&": "&",
        # 128-134
        "€": "€",
        # 129:129,
        "‚": "‚",
        "ƒ": "ƒ",
        "„": "„",
        "…": "…",
        "†": "†",
    }

    d = {
        "\t": "\t",
        "\n": "\n",
        "\r": "\r",
        " ": " ",
        # 39-126
        "'": " ",
        "(": "!",
        ")": '"',
        "*": "#",
        "+": "$",
        ",": "%",
        "-": "&",
        ".": "'",
        "/": "(",
        "0": ")",
        "1": "*",
        "2": "+",
        "3": ",",
        "4": "-",
        "5": ".",
        "6": "/",
        "7": "0",
        "8": "1",
        "9": "2",
        ":": "3",
        ";": "4",
        "<": "5",
        "=": "6",
        ">": "7",
        "?": "8",
        "@": "9",
        "A": ":",
        "B": ";",
        "C": "<",
        "D": "=",
        "E": ">",
        "F": "?",
        "G": "@",
        "H": "A",
        "I": "B",
        "J": "C",
        "K": "D",
        "L": "E",
        "M": "F",
        "N": "G",
        "O": "H",
        "P": "I",
        "Q": "J",
        "R": "K",
        "S": "L",
        "T": "M",
        "U": "N",
        "V": "O",
        "W": "P",
        "X": "Q",
        "Y": "R",
        "Z": "S",
        "[": "T",
        "\\": "U",
        "]": "V",
        "^": "W",
        "_": "X",
        "`": "Y",
        "a": "Z",
        "b": "[",
        "c": "\\",
        "d": "]",
        "e": "^",
        "f": "_",
        "g": "`",
        "h": "a",
        "i": "b",
        "j": "c",
        "k": "d",
        "l": "e",
        "m": "f",
        "n": "g",
        "o": "h",
        "p": "i",
        "q": "j",
        "r": "k",
        "s": "l",
        "t": "m",
        "u": "n",
        "v": "o",
        "w": "p",
        "x": "q",
        "y": "r",
        "z": "s",
        "{": "t",
        "|": "u",
        "}": "v",
        "~": "w",
        # 135-255,
        "‡": "€",
        # 'ˆ']= 129,
        "‰": "‚",
        "Š": "ƒ",
        "‹": "„",
        "Œ": "…",
        # 141]='†',
        "Ž": "‡",
        # 143]='ˆ',
        # 144]='‰',
        "‘": "Š",
        "’": "‹",
        "“": "Œ",
        # '”']=	141,
        "•": "Ž",
        # '–']=	143,
        # '—']=	144,
        "˜": "‘",
        "™": "’",
        "š": "“",
        "›": "”",
        "œ": "•",
        # 157]='–',
        "ž": "—",
        "Ÿ": "˜",
        # 160]='™',
        "¡": "š",
        "¢": "›",
        "£": "œ",
        # '¤']= 157,
        "¥": "ž",
        "¦": "Ÿ",
        # '§']=160,
        "¨": "¡",
        "©": "¢",
        "ª": "£",
        "«": "¤",
        "¬": "¥",
        # 173]='¦',
        "®": "§",
        "¯": "¨",
        "°": "©",
        "±": "ª",
        "²": "«",
        "³": "¬",
        # '´']=173,
        "µ": "®",
        "¶": "¯",
        "·": "°",
        "¸": "±",
        "¹": "²",
        "º": "³",
        "»": "´",
        "¼": "µ",
        "½": "¶",
        "¾": "·",
        "¿": "¸",
        "À": "¹",
        "Á": "º",
        "Â": "»",
        "Ã": "¼",
        "Ä": "½",
        "Å": "¾",
        "Æ": "¿",
        "Ç": "À",
        "È": "Á",
        "É": "Â",
        "Ê": "Ã",
        "Ë": "Ä",
        "Ì": "Å",
        "Í": "Æ",
        "Î": "Ç",
        "Ï": "È",
        "Ð": "É",
        "Ñ": "Ê",
        "Ò": "Ë",
        "Ó": "Ì",
        "Ô": "Í",
        "Õ": "Î",
        "Ö": "Ï",
        "×": "Ð",
        "Ø": "Ñ",
        "Ù": "Ò",
        "Ú": "Ó",
        "Û": "Ô",
        "Ü": "Õ",
        "Ý": "Ö",
        "Þ": "×",
        "ß": "Ø",
        "à": "Ù",
        "á": "Ú",
        "â": "Û",
        "ã": "Ü",
        "ä": "Ý",
        "å": "Þ",
        "æ": "ß",
        "ç": "à",
        "è": "á",
        "é": "â",
        "ê": "ã",
        "ë": "ä",
        "ì": "å",
        "í": "æ",
        "î": "ç",
        "ï": "è",
        "ð": "é",
        "ñ": "ê",
        "ò": "ë",
        "ó": "ì",
        "ô": "í",
        "õ": "î",
        "ö": "ï",
        "÷": "ð",
        "ø": "ñ",
        "ù": "ò",
        "ú": "ó",
        "û": "ô",
        "ü": "õ",
        "ý": "ö",
        "þ": "÷",
        "ÿ": "ø",
    }

    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding="latin1")
    output_stream = io.TextIOWrapper(sys.stdout.buffer, encoding="latin1")

    for line in input_stream:
        for c in line:
            if c in d:
                output_stream.write(d[c])
            elif c in q:
                time.sleep(2)
            else:
                output_stream.write(c)


def a3():
    """https://stackoverflow.com/a/68510869/4072641"""
    s = {k: k - 7 for k in range(128)}
    s[10] = 10
    s[13] = 13
    stdout.write(stdin.read().translate(s))


def a4():
    while 1:
        s = stdin.read(1)
        if s:
            try:
                if ord(s) >= 33 and ord(s) <= 127:
                    print(chr(ord(s) - 7), end="")
                else:
                    print(s, end="")
            except UnicodeError:
                print(s, end="")
        else:
            break


def a5():
    """https://codercodesit.wordpress.com/2012/03/20/uva458-the-decoder/#more-62"""
    try:
        while True:
            b = sys.stdin.buffer.read(1)  # Lê 1 byte de entrada
            if not b:
                break  # Se a entrada estiver vazia, termina o loop
            b = ord(b)  # Converte o byte para o valor inteiro
            if b == 10 or b == 13:
                sys.stdout.buffer.write(bytes([b]))  # Se for '\n' ou '\r', escreve o byte como está
            else:
                sys.stdout.buffer.write(bytes([b - 7]))  # Caso contrário, escreve o byte - 7
    except Exception as e:
        sys.exit(0)


def a6():
    """https://onlinejudge.org/board/viewtopic.php?p=373797&sid=c7357dddc640103bf1a289065608e820#p373797"""
    # Abrindo o stdin com codificação ISO-8859-1
    input_stream = sys.stdin.buffer
    output_stream = sys.stdout.buffer

    while True:
        # Lê uma linha de entrada (com codificação ISO-8859-1)
        input_line = input_stream.readline().decode("ISO-8859-1")

        # Se a linha estiver vazia, termina o loop
        if not input_line:
            break

        # Decodificando cada caractere da linha
        decoded = "".join(chr(ord(c) - 7) for c in input_line)

        # Escrevendo a linha decodificada
        output_stream.write((decoded + "\n").encode("ISO-8859-1"))


def a7():
    # Reading raw bytes from stdin
    byte_data = sys.stdin.buffer.read()

    # Processing the byte data (subtracting 7 from each byte)
    processed_data = bytearray()
    for byte in byte_data:
        processed_data.append(byte)

    # Output the processed data
    sys.stdout.buffer.write(processed_data)


def a8():
    b = sys.stdin.buffer.read(1)
    while b:
        if (
            (b[0] < 39 and b[0] != 10 and b[0] != 13)  # menores que 39, exceto '\n' e '\r'
            or b[0] == 127 + 7  # DEL
            or (b[0] == 129 + 7 or b[0] == 141 + 7 or b[0] == 143 + 7 or b[0] == 144 + 7 or b[0] == 157 + 7)  # não usados
        ):
            time.sleep(3)
        elif b[0] >= 39 and b[0] <= 126:
            result_int = b[0] - 7
            result_byte = bytes([result_int])
            sys.stdout.buffer.write(result_byte)
        else:
            sys.stdout.buffer.write(b)
        # print(b, ord(b), int.from_bytes(b, byteorder="big"),chr(int.from_bytes(b, byteorder="big")))
        b = sys.stdin.buffer.read(1)


if __name__ == "__main__":
    a1()
