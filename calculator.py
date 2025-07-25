import art
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
    return None
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
#print(operations ["*"](4, 8))
def calculator():
    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation:\n ")
        num2 = float(input("Enter next number:\n "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False

# Main program loop
while True:
    calculator()
    if input("Type 'q' to quit or any other key to start a new calculation: ") == 'q':
        break