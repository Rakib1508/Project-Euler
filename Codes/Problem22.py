alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

names = [input().strip() for _ in range(int(input()))]

for _ in range(int(input())):
    name = input().strip()
    res = 0
    items = list(name)
    for c in items:
        res += alphabet.index(c) + 1
    pos = names.index(name) + 1
    print(res * pos)
