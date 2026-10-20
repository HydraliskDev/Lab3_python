def x_iterative(n):
    if n < 1:
        raise ValueError('n должно быть >= 1')
    if n <= 3:
        return 1

    a, b, c = 1, 1, 1
    for _ in range(4, n + 1):
        a, b, c = b, c, a + c
    return c
print(x_iterative(12))