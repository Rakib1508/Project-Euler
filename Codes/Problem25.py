from bisect import bisect_left as splitter

fibonacci = [0] * 23923
fibonacci[1] = 1
fibonacci[2] = 1
digit = [0] * 23923
positional_number = 10
length = 1

for index in range(3, 23923):
    fibonacci[index] = fibonacci[index-1] + fibonacci[index-2]
    if fibonacci[index] < positional_number:
        digit[index] = length
    else:
        positional_number *= 10
        length += 1
        digit[index] = length

for _ in range(int(input())):
    number_of_digits = int(input())
    print(splitter(digit, number_of_digits))
