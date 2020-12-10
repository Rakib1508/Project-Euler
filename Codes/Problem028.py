for i in range(int(input())):
    num = int(input())
    max_gap = (num - 1) // 2
    result  = 4 * ((max_gap * num**2) - (((max_gap - 1) * max_gap * 16) // 2) - ((8 * max_gap * (max_gap - 1) * (max_gap - 2)) // 3)) - (6 * ((num - 1) * (num + 1) // 4)) + 1
    print(int(result%1000000007))
