number = int(input())
power = 10
result = sum(pow(i, i, 10 ** power) for i in range(number + 1))
result = int(str(result)[-10:])
print(result - 1)
