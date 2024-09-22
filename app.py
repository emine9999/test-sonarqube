def greet(name):
    """
    This function greets the person passed in as a parameter
    """
    return f"Hello, {name}!"

def divide(a, b):
    """
    This function divides a by b
    """
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    name = input("Enter your name: ")
    print(greet(name))

    # Potential bug: Using input for numbers without proper validation
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = divide(int(num1), int(num2))
    print(f"Result of division: {result}")

    # Unused variable (SonarQube should catch this)
    unused_var = "This variable is never used"

if __name__ == "__main__":
    main()
