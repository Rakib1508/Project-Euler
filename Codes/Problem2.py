def gen_fib_numbers(lim):
    numbers = [1, 2]
    first = 1
    second = 2
    num = 0
    while first + second < lim:
        num = first + second
        first = second
        second = num
        numbers.append(num)
        
    result = [item for item in numbers if item%2 == 0]
    return result


sums = []
for i in range(int(input())):
    limit = int(input())
    fibs = gen_fib_numbers(limit)
    sums.append(sum(fibs))

[print(item) for item in sums]
