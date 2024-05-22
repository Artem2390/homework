def get_primes(n):
    """Returns a list of prime numbers up to n"""
    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes


primes = get_primes(20)
print(primes)
