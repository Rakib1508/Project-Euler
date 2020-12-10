from itertools import product

def is_palindrome(num):
    return str(num) == str(num)[::-1]


products = []
for _ in range(int(input())):
    number = int(input())
    largest = None
    for i in range(100, 1000):
        for j in range(i, 1000):
            if i * j < 100000:
                continue
            if i * j > number:
                break
            if is_palindrome(i * j):
                largest = i * j
    
    if largest:
        products.append(largest)
        
[print(i) for i in products]
