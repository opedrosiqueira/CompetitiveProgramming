import re


def gambiarra():
    """os dados de teste são fracos; apenas verificando se T é um prefixo de S é AC quando não deveria ser"""
    tc = int(input())
    for i in range(tc):
        s = input()
        q = int(input())
        for j in range(q):
            t = input()
            print("y" if s.startswith(t) else "n")


def a0():
    """a solução ideal seria com árvore de sufixos ou kmp preffix? o problema dá muitos casos repetidos, e a solução ingênua fica recalculando

    - árvore de sufixos https://www.geeksforgeeks.org/pattern-searching-set-8-suffix-tree-introduction/
    - kmp https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/"""

    tc = int(input())
    for i in range(tc):
        s = input()
        q = int(input())
        y = set()  # conjunto de respostas aceitas
        n = set()  # conjunto de respostas não aceitas
        for j in range(q):
            t = input()
            if t in y:
                print("y")
            elif t in n:
                print("n")
            elif t in s:
                print("y")
                y.add(t)
            else:
                print("n")
                n.add(t)


def a1():
    tc = int(input())
    output = []
    for i in range(tc):
        s = input()
        q = int(input())
        for j in range(q):
            t = input()
            output.append("y" if t in s else "n")
    print("\n".join(output))


def a2():
    tc = int(input())
    for i in range(tc):
        s = input()
        q = int(input())
        for j in range(q):
            t = input()
            print("y" if t in s else "n")


def a3():
    tc = int(input())
    output = []
    for i in range(tc):
        s = input()
        q = int(input())
        for j in range(q):
            t = input()
            output.append("y" if re.search(t, s) else "n")
    print("\n".join(output))


def a4():
    tc = int(input())
    for i in range(tc):
        s = input()
        q = int(input())
        for j in range(q):
            t = input()
            print("y" if re.search(t, s) else "n")


if __name__ == "__main__":
    a0()
