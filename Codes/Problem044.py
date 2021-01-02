def generator(i, k, v):
    if v == 'sub':
        return ((i * (3 * i - 1)) / 2) - (((i - k) * (3 * (i - k) - 1)) / 2)
    else:
        return ((i * (3 * i - 1)) / 2) + (((i - k) * (3 * (i - k) - 1)) / 2)


def formatter(left, right):
    num1 = (1 + (1 - 4 * 3 * (-2) * left)**0.5) / 6
    num2 = (1 + (1 - 4 * 3 * (-2) * right)**0.5) / 6
    return num1 == int(num1) or num2 == int(num2)


n, k = map(int, input().split())
for i in range(k+1, n+1):
    left = generator(i, k, 'sub')
    right = generator(i, k, 'add')
    if formatter(left, right):
        print((i * (3 * i - 1)) // 2)
