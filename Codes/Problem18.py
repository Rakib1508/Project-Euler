results = []
for _ in range(int(input())):
    triangle = []
    for _ in range(int(input())):
        row = list(map(int, input().split()))
        triangle.append(row)
    
    index = 0
    add = 0
    for i in range(len(triangle)):
        if len(triangle[i]) == 1:
            add += triangle[i][0]
            continue
        
        if triangle[i][index] > triangle[i][index+1]:
            add += triangle[i][index]
        else:
            add += triangle[i][index+1]
            index = index+1
    
    results.append(add)

[print(a) for a in results]
