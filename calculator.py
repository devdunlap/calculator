import art
import math

print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Cannot divide by zero!"

def get_number(prompt):
    """Get a valid number from user input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def get_operation():
    """Get a valid operation from user input."""
    while True:
        operation = input("Pick an operation: ").strip()
        if operation in operations:
            return operation
        else:
            print(f"❌ Invalid operation! Please choose from: {', '.join(operations.keys())}")

def get_yes_no_input(prompt):
    """Get a valid yes/no input from user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("❌ Please enter 'y' for yes or 'n' for no.")

def power(n1, n2):
    return n1 ** n2

def square_root(n1, n2=None):
    if n1 >= 0:
        return math.sqrt(n1)
    else:
        return "Error: Cannot calculate square root of negative number!"

def percentage(n1, n2):
    return (n1 / 100) * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "√": square_root,
    "%": percentage
}
#print(operations ["*"](4, 8))
def calculator():
    print("\n" + "="*50)
    print("🧮 CALCULATOR STARTED")
    print("="*50)
    
    num1 = get_number("Enter first number: ")
    
    print("\nAvailable operations:")
    operation_names = {
        "+": "Addition", 
        "-": "Subtraction", 
        "*": "Multiplication", 
        "/": "Division",
        "^": "Power (x^y)",
        "√": "Square Root (√x)",
        "%": "Percentage (x% of y)"
    }
    for symbol in operations:
        print(f"  {symbol} - {operation_names.get(symbol, symbol)}")
    
    should_continue = True
    while should_continue:
        print(f"\nCurrent number: {num1}")
        operation_symbol = get_operation()
        
        # Square root only needs one number
        if operation_symbol == "√":
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1)
            result_text = f"√{num1} = {answer}"
            print(f"\n✅ {result_text}")
            calculation_history.append(result_text)
        else:
            num2 = get_number("Enter next number: ")
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            
            # Handle errors
            if isinstance(answer, str) and "Error" in answer:
                print(f"❌ {answer}")
                continue
            
            result_text = f"{num1} {operation_symbol} {num2} = {answer}"
            print(f"\n✅ {result_text}")
            calculation_history.append(result_text)
        
        # Handle errors for square root
        if isinstance(answer, str) and "Error" in answer:
            print(f"❌ {answer}")
            continue
        
        continue_with_result = get_yes_no_input(f"\nType 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ")
        
        if continue_with_result:
            num1 = answer
        else:
            should_continue = False
    
    print("🏁 Calculation session ended.\n")

# Main program loop
calculation_history = []

def show_history():
    """Display calculation history."""
    if not calculation_history:
        print("📋 No calculations in history yet.")
        return
    
    print("\n📋 CALCULATION HISTORY")
    print("="*30)
    for i, calc in enumerate(calculation_history, 1):
        print(f"{i}. {calc}")
    print("="*30)

while True:
    calculator()
    
    # Ask if user wants to see history
    if calculation_history:
        show_hist = get_yes_no_input("Would you like to see your calculation history? (y/n): ")
        if show_hist:
            show_history()
    
    # Ask to continue or quit
    print("\nOptions:")
    print("  'q' - Quit calculator")
    print("  'h' - Show history")
    print("  Any other key - Start new calculation")
    
    choice = input("Your choice: ").strip().lower()
    
    if choice == 'q':
        print("👋 Thank you for using the calculator! Goodbye!")
        break
    elif choice == 'h':
        show_history()