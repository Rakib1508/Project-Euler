def is_prime(n):
    for a in range(3, int(n**0.5)+1, 2):
        if n%a == 0:
            return False
    return True


def get_primes(num):
    primes = [2, 3]
    for i in range(5, num, 2):
        if is_prime(i):
            primes.append(i)
    return primes


prime_sum = []
for _ in range(int(input())):
    next_number = int(input())
    prime_sum.append(sum(get_primes(next_number + 1)))
    
[print(a) for a in prime_sum]
