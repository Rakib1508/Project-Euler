from math import factorial

result = 0
for i in range(10, int(input())):
    fact = 0
    for j in str(i):
        fact += factorial(int(j))
    if fact % i == 0:
        result += i
print(result)
