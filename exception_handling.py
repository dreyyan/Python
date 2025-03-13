def exception_division(x, y):
    try: # Prone-error code
        quotient = x / y
    except ZeroDivisionError: # Error type
        print("Division by zero is not allowed.")
    else: # No errors
        print(f'{x} / {y} = {quotient}')
    finally: # Always executes
        print("Divison completed.")

exception_division(5, 0)