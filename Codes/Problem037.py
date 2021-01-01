import math

def sieve_of_Eratosthenes(n):
    nums = list(range(2, n + 1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i - 2] != 0:
            for j in range(i - 2 + i, n - 2 + 1, i):
                nums[j] = 0
    return [x for x in nums if x != 0]


def get_left_and_right(n, primes):
    n_left = n
    n_right = 0
    i = 0
    while n_left % 10 != n_left:
        n_right += (n_left % 10) * (10 ** i)
        n_left //= 10
        i += 1
        if not n_right in primes or not n_left in primes:
            return False
    return True


number = int(input())
primes = set(sieve_of_Eratosthenes(number))
result = 0
for i in primes:
    if i > 7 and get_left_and_right(i, primes):
        result += i
print(result)
