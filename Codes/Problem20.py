from math import factorial
for _ in range(int(input())):
    number = int(input())
    string = str(factorial(number))
    digits = (int(c) for c in string)
    print(sum(digits))
