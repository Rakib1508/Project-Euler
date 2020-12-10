def compute_sum(power, lower, upper):
    add = 0
    for i in range(lower, upper):
        digits = list(map(int, str(i)))
        temp = 0

        for j in digits:
            temp += j**power
        
        if i == temp:
            add += i
            
    return add


num = int(input())
if num == 3:
    lower, upper = 10**2, 10**3
elif num == 4:
    lower, upper = 10**3, 10**4  
elif num == 5:
    lower, upper = 2*(10**3), 2*(10**5)
elif num == 6:
    lower, upper = 10**5, 6*(10**5)

result = compute_sum(num, lower, upper)
print(result)
