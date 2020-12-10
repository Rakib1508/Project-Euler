def find_greatest_prime(n):
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
    return n


prime = []
for _ in range(int(input())):
    num = int(input())
    prime.append(find_greatest_prime(num))
    
[print(i) for i in prime]
