results = []
for _ in range(int(input())):
    added_sum = int(input())
    stamp = -1
    
    for a in range(3, (added_sum//3)+1):
        b = (added_sum**2 - 2*a*added_sum)//(2*added_sum - 2*a)
        c = added_sum - b - a
        
        if a**2 + b**2 == c**2:
            if a*b*c > stamp:
                stamp = a*b*c
    
    results.append(stamp)

[print(a) for a in results]
