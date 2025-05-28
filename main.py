from calculator.core.calculator import Calculator
import shlex # For simple parsing of input

def main():
    calc = Calculator()
    print("Simple CLI Calculator")
    print("Enter expressions, or 'quit'/'exit' to exit.")
    print("Supported operations: +, -, *, /")
    print("Supported scientific functions: sin, cos, tan, asin, acos, atan, log, log10, power")
    print("Other commands: clear, ms (memory store), mr (memory recall), mc (memory clear)")
    print("Example: '5' (sets current value to 5)")
    print("         '+ 3' (adds 3 to current value)")
    print("         'sin' (calculates sine of current value)")
    print("         'power 2' (calculates current value to the power of 2)")


    while True:
        try:
            user_input = input(f"[{calc.get_current_value()}] > ").strip().lower()

            if user_input in ["quit", "exit"]:
                print("Exiting calculator.")
                break

            parts = shlex.split(user_input) # Use shlex for basic tokenization
            command = parts[0] if parts else ""
            
            if not command:
                continue

            if command == "clear":
                calc.clear()
            elif command == "ms":
                calc.memory_store()
                print("Value stored in memory.")
            elif command == "mr":
                calc.memory_recall()
            elif command == "mc":
                calc.memory_clear()
                print("Memory cleared.")
            elif command in ["+", "add", "plus"]:
                if len(parts) > 1:
                    try:
                        num = float(parts[1])
                        calc.add(num)
                    except ValueError:
                        print("Invalid number for addition.")
                else:
                    print("Usage: + <number>")
            elif command in ["-", "subtract", "minus"]:
                if len(parts) > 1:
                    try:
                        num = float(parts[1])
                        calc.subtract(num)
                    except ValueError:
                        print("Invalid number for subtraction.")
                else:
                    print("Usage: - <number>")
            elif command in ["*", "multiply", "times"]:
                if len(parts) > 1:
                    try:
                        num = float(parts[1])
                        calc.multiply(num)
                    except ValueError:
                        print("Invalid number for multiplication.")
                else:
                    print("Usage: * <number>")
            elif command in ["/", "divide", "div"]:
                if len(parts) > 1:
                    try:
                        num = float(parts[1])
                        calc.divide(num)
                    except ValueError as e:
                        print(f"Error: {e}")
                    except ZeroDivisionError: # Should be caught by calc.divide
                        print("Error: Cannot divide by zero.")
                else:
                    print("Usage: / <number>")
            elif command == "power":
                if len(parts) > 1:
                    try:
                        exponent = float(parts[1])
                        calc.power(exponent)
                    except ValueError:
                        print("Invalid number for exponent.")
                else:
                    print("Usage: power <exponent>")
            elif command == "log":
                calc.log()
            elif command == "log10":
                calc.log10()
            elif command == "sin":
                calc.sin()
            elif command == "cos":
                calc.cos()
            elif command == "tan":
                calc.tan()
            elif command == "asin":
                calc.asin()
            elif command == "acos":
                calc.acos()
            elif command == "atan":
                calc.atan()
            else:
                # Try to interpret as a number to set current_value
                try:
                    num = float(command)
                    calc.current_value = num # Directly set current value
                    if len(parts) > 1: # If there's more after the number, it's an invalid command
                        print(f"Unknown command or invalid format: '{user_input}'. Number part '{command}' was set as current value, rest ignored.")
                except ValueError:
                    print(f"Unknown command: {command}")
            
            # Display current value after each operation unless it was a memory store/clear or error
            if command not in ["ms", "mc"] and "Error" not in command : # Avoid printing if there was an error message already
                # Check if an error occurred in the calculator method itself
                if isinstance(calc.get_current_value(), str) and "Error" in calc.get_current_value():
                     print(calc.get_current_value()) # Should be handled by exception blocks now
                # else:
                #    print(f"Result: {calc.get_current_value()}") # Redundant due to prompt

        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
