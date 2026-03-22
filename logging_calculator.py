import logging

# Setup logging
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Calculator started")

def add(a, b):
    result = a + b
    logging.info(f"Addition: {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logging.info(f"Subtraction: {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"Multiplication: {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        return "Error: Cannot divide by zero"

def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "5":
            logging.info("Calculator exited")
            print("Goodbye!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            logging.error("Invalid number input")
            print("Invalid input! Please enter numbers.")
            continue

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        else:
            logging.warning("Invalid menu choice")
            print("Invalid choice!")

calculator()