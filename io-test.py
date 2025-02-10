import io
import os
import sys


def a0():
    r = os.read(0, 2**32)
    output = []
    for line in r.splitlines():
        output.append(line)
    os.write(1, "\n".join(output))


def a1():
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding="latin1")
    output_stream = io.TextIOWrapper(sys.stdout.buffer, encoding="latin1")
    for line in input_stream:
        output_stream.write(line)


def a2():
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding="latin1")
    output_stream = io.TextIOWrapper(sys.stdout.buffer, encoding="latin1")
    data = input_stream.readlines()
    result = []
    for line in data:
        result.append(line)
    output_stream.write("".join(result))


def a3():
    for line in sys.stdin:
        sys.stdout.write(line)


def a4():
    data = sys.stdin.readlines()
    results = []
    for line in data:
        results.append(line)
    sys.stdout.write("".join(results))


def a5():
    for line in sys.stdin.buffer:
        sys.stdout.buffer.write(line)


def a6():
    data = sys.stdin.buffer.readlines()
    results = []
    for line in data:
        results.append(line)
    sys.stdout.buffer.write(b"".join(results))
