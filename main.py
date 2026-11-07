# Simple calculator - python project
def add_numbers(first_number, second_number):
    """Returns the sum of two numbers."""
    return first_number + second_number


def subtract_numbers(first_number, second_number):
    """Returns the difference between two numbers."""
    return first_number - second_number


def multiply_numbers(first_number, second_number):
    """Returns the product of two numbers."""
    return first_number * second_number


def divide_numbers(first_number, second_number):
    """Divides two numbers and handles division by zero."""
    if second_number == 0:
        return "Cannot divide using 0."
    
    return first_number / second_number


def modulus_numbers(first_number, second_number):
    """Returns the remainder and handles modulus by zero."""
    if second_number == 0:
        return "Cannot operate modulus using 0."
    
    return first_number % second_number

print(add_numbers.__doc__)
print(subtract_numbers.__doc__)
print(multiply_numbers.__doc__)
print(divide_numbers.__doc__)
print(modulus_numbers.__doc__)

if __name__ == "__main__":
    while True:
        print("\n===== BASIC CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        try:
            choice = int(input("Select an operator: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 6:
            print("Goodbye!")
            break

        elif 1 <= choice <= 5:
            try: 
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == 1:
                print("Result:", add_numbers(first_number, second_number))

            elif choice == 2:
                print("Result:", subtract_numbers(first_number, second_number))

            elif choice == 3:
                print("Result:", multiply_numbers(first_number, second_number))

            elif choice == 4:
                print("Result:", divide_numbers(first_number, second_number))

            elif choice == 5:
                print("Result:", modulus_numbers(first_number, second_number))
        else:
            print("Invalid choice! Please select between 1 and 6.")
