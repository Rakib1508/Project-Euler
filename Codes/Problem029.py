num = int(input())

top = 1
while(pow(2, top) <= num):
    top += 1
max_gap = top

numbers = {}
for i in range(1, max_gap):
    numbers[i]=[]
    for j in range(2, num+1):
        numbers[i].append(j*i)
    if(i != 1):
        temp = list(set().union(numbers[i-1], numbers[i]))
        numbers[i] = temp

check = []
for i in range(2, num+1):
    check.append(0)

ans = 0
for i in range(2, num+1):
    if(check[i-2] == 0):
        check[i-2] = 1
        j = i*i
        while(j <= num):
            check[j-2] = 1
            j = j*i
        
        k=1
        while(pow(i, k) <= num):
            k += 1
        max_gap = k
        ans += len(numbers[k-1])

print(ans)
