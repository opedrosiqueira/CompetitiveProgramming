from sys import stdin

for line in stdin:
    numbers = list(map(int, line.split()))  # converte uma string de números para uma lista de números
    jolly_jumpers = [False] * numbers[0]  # o numbers[0] é o comprimento da sequência
    for i in range(2, len(numbers)):  # como compara com o anterior, deve começar do segundo
        diff = abs(numbers[i] - numbers[i - 1])
        if diff < numbers[0]:
            jolly_jumpers[diff] = True

    is_jolly = True
    for i in range(1, numbers[0]):  # os índices jolly jumpers vão de 1 até n-1
        if jolly_jumpers[i] is False:
            is_jolly = False
            break
    print("Jolly" if is_jolly else "Not jolly")
