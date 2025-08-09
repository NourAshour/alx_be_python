def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        print(num / den)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")