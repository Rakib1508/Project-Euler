from math import factorial as fact

tc = int(input())
for i in range(tc):
    m, n = map(int, input().split())
    print((fact(m + n) // (fact(m) * fact(n))) % 1000000007)
