import sys

cache = 5000001
final = [0] * cache
final[0] = 1

def sequence_list(start):
    if start < cache and final[start-1] != 0:
        return final[start-1]
    else:
        result = 0
        if start%2 == 0:
            result = 1 + sequence_list(start >> 1)
        else:
            result = 1 + sequence_list(3*start + 1)
        
        if start < cache:
            final[start-1] = result
            
    return result

    
for i in range(1, cache):
    sequence_list(i)
    
for _ in range(int(input())):
    number = int(input().strip())
    print(number - final[0:number][::-1].index(max(final[0:number])))
