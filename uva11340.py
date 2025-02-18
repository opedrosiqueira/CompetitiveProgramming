# Esse artigo fala sobre a entrada ser iso8859-1 (latin1): https://www.redgreencode.com/solving-uva-11340-in-java/. O udebug diz que apenas nos artigos há caracteres binários (não ASCII), na tabela não há.
#
# Como a entrada é muito grande, parece que `input()`/`print()` não são suficientemente rápidos. A solução pode ser usar `sys.stdin.buffer` e `sys.stdout.buffer` para ler e escrever bytes, e `io.TextIOWrapper` para converter bytes em strings.
#
# Tentei usando tanto dicionário quanto endereçamento direto, e por incrível que pareça, medindo tempo com `-m cProfile`, endereçamento direto é pior que dicionário, por conta da chamada à função `ord()`.


def alternativa0():
    """versão mais rápida. lê todos os dados de uma vez e escreve tudo de uma vez."""

    import io, sys
    from collections import defaultdict, Counter

    data = io.TextIOWrapper(sys.stdin.buffer, encoding="latin1").readlines()
    results = []

    n = int(data[0])
    index = 1

    for _ in range(n):
        k = int(data[index])
        index += 1

        char_values = defaultdict(int)
        for _ in range(k):
            line = data[index]
            index += 1
            char, value = line[0], int(line[2:])
            char_values[char] = value

        m = int(data[index])
        index += 1
        total_payment = 0

        article = "".join(data[index : index + m])
        index += m
        char_count = Counter(article)
        for char, count in char_count.items():
            total_payment += char_values[char] * count

        results.append(f"{(total_payment / 100):.2f}$")

    sys.stdout.write("\n".join(results) + "\n")


def alternativa1():
    """versão suficientemente rápida. lê e escreve linha a linha."""

    import io, sys
    from collections import defaultdict

    read = io.TextIOWrapper(sys.stdin.buffer, encoding="iso-8859-1").readline
    write = io.TextIOWrapper(sys.stdout.buffer, encoding="iso-8859-1").write

    n = int(read())

    for _ in range(n):
        k = int(read())

        char_values = defaultdict(int)
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


def alternativa2():
    """versão lenta. não dá pra usar o padrão input() e print()."""
    from collections import defaultdict

    n = int(input())

    for _ in range(n):
        k = int(input())

        char_values = defaultdict(int)
        for _ in range(k):
            char, value = input().split()
            char_values[char] = int(value)

        m = int(input())
        total_payment = 0

        for _ in range(m):
            article_line = input()
            for char in article_line:
                total_payment += char_values[char]

        print(f"{(total_payment / 100):.2f}$")


def alternativa3():
    import io, sys, array

    read = io.TextIOWrapper(sys.stdin.buffer, encoding="iso-8859-1").readline
    write = io.TextIOWrapper(sys.stdout.buffer, encoding="iso-8859-1").write

    n = int(read())

    for _ in range(n):
        k = int(read())

        char_values = [0] * 256  # `[0] * size` eh mais rapido que `[0 for _ in range(size)]`
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


if __name__ == "__main__":
    alternativa1()
