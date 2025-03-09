def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    print(f"{number} is a prime number.")
    return True


prime = int(input("Ask for a number:    "))
is_prime(prime)

