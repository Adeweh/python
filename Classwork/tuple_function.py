def is_prime(num: int) -> bool:
    import math

    if num <= 1:
        return False
    if num == 2:
        return True

    max_divisor = math.ceil(math.sqrt(num)) + 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False

    return True


primes = sum(i for i in range(1, 10_000_000) if is_prime(i)) # will take a while to load cuz of the many numbers
print(primes)
