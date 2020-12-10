string = 'abcdefghijklm'

def find_factorial(num):
    x = 1
    while num != 0:
        fac[13 - x] = num % x
        num = num // x
        x += 1
    return fac


def find_pos(fac):
    array = list(string)
    output = ''
    for i in range(len(fac)):
        output += array.pop(fac[i])
    return output


for _ in range(int(input())):
    fac = [0] * 13
    number = int(input()) - 1
    fac = find_factorial(number)
    print(find_pos(fac))
