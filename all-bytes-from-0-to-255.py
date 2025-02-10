import sys

file_name = input("Enter file name: ") or "all-bytes-from-0-to-255.bin"


def writoToFile():
    with open(file_name, "wb") as f:
        # for i in range(2**12):
            f.write(b"\t\r\n")
            f.write(bytes(range(32, 127)))
            f.write(b"\x80")
            f.write(bytes(range(130, 141)))
            f.write(b"\x8e")
            f.write(bytes(range(145, 157)))
            f.write(bytes(range(158, 256)))


def readFromFile():
    with open(file_name, "rb") as f:
        print(f.read())


def readFromStdin():
    b = sys.stdin.buffer.read(1)
    while b:
        print(b, b[0], ord(b), int.from_bytes(b, byteorder="big"), chr(int.from_bytes(b, byteorder="big")))
        b = sys.stdin.buffer.read(1)


if __name__ == "__main__":
    writoToFile()
    # readFromFile()
    # readFromStdin()
