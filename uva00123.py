from sys import stdin

ignore = set()
line = stdin.readline()
while line != "::\n":
    ignore.add(line.rstrip().lower())
    line = stdin.readline()

alist = []
count = 0  # como títulos com mesmas palavras-chaves são ordenados por quem veio primeiro, eu mantenho a ordem das inserções nessa variável
for line in stdin:
    start = 0
    line = line.lower()
    for end in range(len(line)):  # para cada índice de line
        if line[end].isspace():  # se for espaço, então terminou a palavra atual
            if line[start].isalpha() and line[start:end] not in ignore:  # se a palavra atual não estiver nas ignoradas
                alist.append((line[start:end], count, line[0:start] + line[start:end].upper() + line[end:]))  # adiciona essa frase na lista, com a palavra atual em maiúsculo
                count += 1
            start = end + 1

alist.sort()  # ao ordenar tuplas, o padrão é ordenar pelo primeiro campo, quando houver empate, desempata pelo segundo campo, e assim sucessivamente. se não houvesse o campo `count`, os empates seriam desempatados pela ordem alfabética dos títulos, que não é o que o enunciado pediu.

for item in alist:
    print(item[2], end="")
