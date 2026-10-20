def x_recursive(n: int) -> int:
    if n < 1:
        raise ValueError('n должно быть >= 1')
    if n <= 3:
        return 1
    return x_recursive(n - 1) + x_recursive(n - 3)
print(x_recursive(12))