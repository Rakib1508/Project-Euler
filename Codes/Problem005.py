def find_LCM(a, b):
    if a > b:
        greater = a
    else:
        greater = b
        
    while True:
        if greater%a == 0 and greater%b == 0:
            return greater
        else:
            greater += 1
        
    return greater

    
numbers = []
for _ in range(int(input())):
    lcm = 1
    num = int(input())
    for i in range(2, num + 1):
        lcm = find_LCM(lcm, i)
    numbers.append(lcm)
    
[print(n) for n in numbers]
