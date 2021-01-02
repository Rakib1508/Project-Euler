n, a, b = map(int, input().split())

if a == 3 and b == 5:
    t = 1
    p = 1
    while t * (t + 1) / 2 < n:
        if t > 0:
            print(t * (t + 1) // 2)
        prev_t = t
        prev_p = p
        t = -2 * prev_t - 3 * prev_p - 1
        p = -1 * prev_t - 2 * prev_p

if a == 5 and b == 6:
    p = 1
    h = 1
    while h * (2 * h - 1) < n:
        print(h * (2 * h - 1))
        prev_p = p
        prev_h = h
        p = 97 * prev_p + 112 * prev_h - 44
        h = 84 * prev_p + 97 * prev_h - 38
