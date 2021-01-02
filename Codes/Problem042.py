def is_triangle_number(num):
    t_sum = (-1 + (1 + 8 * num)**0.5) / 2
    if t_sum == int(t_sum):
        return int(t_sum)
    else:
        return -1


for _ in range(int(input())):
    number = int(input())
    print(is_triangle_number(number))
