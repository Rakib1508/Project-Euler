def abundant(num):
    total = 0
    for i in range(2, int(num**0.5)+1):
        if(num%i == 0):       
            if(i != num/i):
                total += i + (num / i)
            else:
                total += i
            
    if(num < total+1):
        return True
    else:
        return False


for i in range(int(input())):
    number = int(input())
    indicator = True
    for i in range(2, (number//2) + 1):
        if(abundant(i) and abundant(number - i)):
            print("YES")
            indicator = False
            break
    
    if indicator:
        print("NO")
