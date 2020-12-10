def find_recursion(num):
    signal = [0]*num
    signal[1] = 1
    dividand = 1
    i = 2
    while (True):
        dividand *= 10
        remainder = dividand % num
        if remainder == 0:
            return 0
        if signal[remainder]:
            return i - signal[remainder]
        signal[remainder] = i
        i += 1
        dividand = remainder


response = [0]*10000
length = [0]*10000
response[3] = 3
response[4] = 3
length[4] = 1
length[3] = 1

for i in range(5, 10000):
    sequence = find_recursion(i)
    if sequence > length[response[i - 1]]:
        response[i] = i
        length[i] = sequence
    else:
        response[i] = response[i - 1]
        length[i] = length[i - 1]

for _ in range(int(input())):
    number = int(input())
    print(response[number - 1])
