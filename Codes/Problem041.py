from itertools import permutations  
from bisect import bisect_left

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num < 2:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num%i == 0:
            return False
    return True


def pandigital_prime():
    perm_tuples = []
    for i in range(2, 10):
        perm = list(permutations(range(1, i+1)))
        perm_tuples += perm
    
    perm_nums = []
    for i in perm_tuples:
        num = int(''.join([str(j) for j in i]))
        perm_nums.append(num)
    
    primes = []
    for i in perm_nums:
        if is_prime(i) == True:
            primes.append(i)
    
    primes.sort()
    return primes
  

primes = pandigital_prime()
for _ in range(int(input())):
    number = int(input())
    idx = bisect_left(primes, number)
    
    if idx<len(primes) and primes[idx] <= number:
        print(primes[idx])
    elif primes[idx-1] <= number:
        print(primes[idx-1])
    else:
        print(-1)
