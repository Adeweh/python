def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print(is_prime(113))


def is_prime(num: int) -> bool:
    max_divisor = (num // 2) * 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False

    return True


print(is_prime(113))


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


print(is_prime(6))

primes = [i for i in range (1,101) if is_prime(i)]
print(primes)
