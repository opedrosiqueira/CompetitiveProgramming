from math import floor, sqrt


tc = int(input())
for _ in range(tc):
    S_n = int(input())
    # S_n <= n(a_1+a_n)/2
    # S_n <= n(1+n)/2
    # n^2 + n - 2S_n <= 0
    # n <= (-b +- \sqrt{b^2-4ac})/2a
    # n <= (-1 +- \sqrt{1-4*(-2S_n)})/2
    # n <= (-1 + \sqrt{1+8S_n})/2 # como quero números positivos, então calculo só a raiz positiva
    i = (-1 + sqrt(1 + 8 * S_n)) / 2
    print(floor(i))
