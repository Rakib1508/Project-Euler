for _ in range(int(input())):
    up_limit = int(input())
    numbers = [i for i in range(1, up_limit) if i%3 == 0 or i%5 == 0]
    print(sum(numbers))
