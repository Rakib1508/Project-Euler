from itertools import permutations

def substringify():
    items = (int(''.join(map(str, num))) for num in permutations(range(n+1)) if divisibility_test(num))
    return sum(items)


def divisibility_test(num):
    numbers = ((num[i+1] * 100 + num[i+2] * 10 + num[i+3])%p == 0 for i, p in enumerate(divisible[:n-2]))
    return all(numbers)


divisible=[2,3,5,7,11,13,17]
n=int(input())
print(substringify())
