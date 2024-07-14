def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        result = numerator/denominator
        print(f"The result of the division is {result}")
        
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
    
    try:
        result = numerator/denominator
        return result
    except ValueError:
        print(f"Error: Please enter numeric values only.")