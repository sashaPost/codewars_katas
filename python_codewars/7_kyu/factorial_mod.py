def factorial(n):
    if n > 12:
        raise ValueError
    elif 0 <= n < 2:
        return 1
    elif n < 0:
        raise ValueError
    return n * factorial(n - 1) 