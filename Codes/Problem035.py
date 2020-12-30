number = int(input())
primes = []

for i in range(number):
    primes.append(True)

for i in range(2, number//2):
    if primes[i] == True:
        for j in range(i * i, number, i):
            primes[j] = False

primes[1] = False
result = 0

for i in range(number):
    j = 0
    string = str(i)
    while j < len(str(i)):
        string = str(i)[j:] + str(i)[:j]
        j += 1
        if not primes[int(string)]:
            break
    else:
        result += i

print(result)
