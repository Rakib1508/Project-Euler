result = []
for _ in range(int(input())):
    num = int(input())
    s = num
    square_sum = (num * (num+1) * (2*num+1)) // 6
    triangle_sum = (num * (num+1)) // 2
    sum_square = triangle_sum ** 2
    result.append(sum_square - square_sum)
    
[print(i) for i in result]
