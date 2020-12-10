def is_prime(num):
    if num in [2, 3]:
        return True
    if num < 2 or num%2 == 0:
        return False
    if num < 9:
        return True
    if num%3 == 0:
        return False
    
    last = int(num**0.5)
    i = 5
    while(i <= last):
        if num%i == 0:
            return False
        if num%(i+2) == 0:
            return False
        i +=6
    return True  


param1=0
param2=0
count=0
number = int(input())

for y in range(1, number):
    for x in range(-number, 0):
        length = 0
        while(is_prime(length**2 + x*length + y)):
            length += 1
        if(length>count):
            param1, param2 = x, y
            count = length

print(param1, param2)
