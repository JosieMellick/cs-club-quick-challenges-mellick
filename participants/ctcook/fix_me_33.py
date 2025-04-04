def is_prime(n):
    if n < 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False
