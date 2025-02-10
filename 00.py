import io, sys


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


if __name__ == "__main__":
    a1()
