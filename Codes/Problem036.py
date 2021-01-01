def valid(n, k):
    string = ''
    while n:
        n, x = divmod(n, k)
        string += str(x)
    return string[::-1]


n, k = map(int, input().split())
result = 0
for c in range(1, n+1):
    if str(c) == str(c)[::-1]:
        string = valid(c, k)
        if string == string[::-1]:
            result += c
print(result)
