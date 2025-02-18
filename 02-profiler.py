from collections import defaultdict
import sys

# imprime a média dos tempos de execução de cada função em um arquivo `.prof`, gerado pelo script `01-profiler.py`

# Dados fornecidos
data = open(sys.argv[1]).read()

# Processamento dos dados
values = defaultdict(list)

for line in data.strip().split("\n"):
    value, key = line.split(";")
    values[key].append(float(value))

# Calculando as médias
averages = {key: sum(vals) / len(vals) for key, vals in values.items()}
for key, avg in averages.items():
    print(f"{key};{avg:f}")
