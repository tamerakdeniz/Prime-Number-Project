from art import logo


def is_prime(number):
    """
    Check if a number is prime.
    Args:
        number (int): The number to check
    Returns:
        bool: True if prime, False otherwise
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number <= 1:
        return False
        
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_user_input():
    """Get and validate user input."""
    while True:
        try:
            number = input("\nEnter a number to check if it's prime (or 'q' to quit): ")
            if number.lower() == 'q':
                return None
            return int(number)
        except ValueError:
            print("❌ Please enter a valid integer!")

def main():
    """Main program loop."""
    print(logo)  # Add this line to display the logo
    print("This program checks if a number is prime.")
    
    while True:
        number = get_user_input()
        if number is None:
            print("\nThanks for using Prime Number Checker! Goodbye! 👋")
            break
            
        try:
            if is_prime(number):
                print(f"✅ {number} is a prime number!")
            else:
                print(f"❌ {number} is not a prime number.")
        except TypeError as e:
            print(f"Error: {e}")
            
        print("------------------------------------")

if __name__ == "__main__":
    main()