def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes


def get_sum_of_primes(primes):
    return sum(primes)


def get_multiplication_of_primes(primes):
    result = 1
    for prime in primes:
        result *= prime
    return result


start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

prime_numbers = get_primes_in_range(start_range, end_range)
print("Prime numbers in the range:", prime_numbers)

calculate_sum = input("Do you want to calculate the sum of prime numbers? (yes/no): ")
if calculate_sum.lower() == "yes":
    sum_of_primes = get_sum_of_primes(prime_numbers)
    print("Sum of prime numbers:", sum_of_primes)

calculate_multiplication = input("Do you want to calculate the multiplication of prime numbers? (yes/no): ")
if calculate_multiplication.lower() == "yes":
    multiplication_of_primes = get_multiplication_of_primes(prime_numbers)
    print("Multiplication of prime numbers:", multiplication_of_primes)
