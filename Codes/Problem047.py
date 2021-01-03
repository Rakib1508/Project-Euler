def sieve(n):
    array = [0] * (1+n)
    for i in range(2, 1+n):
        if array[i]:
            continue
        for j in range(i, 1+n, i):
            array[j] += 1
    return array


is_prime = sieve(2000 * 1000)
n, k = map(int, input().split())
for i in range(2, n+1):
    flag = False
    for j in range(k):
        if is_prime[i+j] != k:
            flag = True
            break
    if not flag:
        print(i)
