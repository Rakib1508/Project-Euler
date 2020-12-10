primes = [0,2,3]

def is_prime(num):
    i = 2
    while i <= int(num**0.5)+1:
        if num % i == 0 and num != i:
            return False
        i += 1
    return True


for _ in range(int(input())):
    position = int(input())
    try:
        if primes[position]:
            print(primes[position])
    except:
        ptr = len(primes)
        i = ptr - 1
        num = primes[i]+1
        while ptr <= position:
            if is_prime(num):
                primes.append(num)
                ptr += 1
            num += 1
        print(primes[position])
