def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Error! Division by zero." if b == 0 else a / b

def power(a, b):
    return a ** b

def calculator():
    print("\n========== SIMPLE CALCULATOR ==========")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (**)")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("👋 Exiting Calculator. Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("⚠️ Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter numeric values.")
            continue

        operations = {
            "1": ("Addition", add),
            "2": ("Subtraction", subtract),
            "3": ("Multiplication", multiply),
            "4": ("Division", divide),
            "5": ("Power", power)
        }

        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)

        print(f"🧮 {operation_name} result: {result}")

if __name__ == "__main__":
    calculator()

