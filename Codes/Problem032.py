import re

distinct_items = set()
addition = 0
number = int(input())

for i in range(1964,1,-1):
    for j in range(100):
        if j not in distinct_items:
            product = i * j
            string = str(product) + str(i) + str(j)
            
            if product not in distinct_items:
                matcher = ''.join(str(k) for k in range(1, number+1))             
                
                if(re.fullmatch(matcher, ''.join(sorted(string)))):
                    addition = addition + product                   
                    distinct_items.add(product)
                    
print(addition)
