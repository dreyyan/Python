class ZeroDividendError(Exception):
    def __init__(self, message="ERROR: Undefined"):
        super().__init__(message)

def divide(num1, num2) -> None:
    try:
        if num1 == 0:
            raise ZeroDivisionError
        if num2 == 0:
            raise ZeroDividendError()

        quotient: int = num1 / num2

    except ZeroDividendError:
        print("ERROR: Undefined")
    except ZeroDivisionError:
        print("ERROR: Division by 0 is not allowed.")
    else:
        print(f"{num1} / {num2} = {quotient}")

divide(5, 0)
divide(0, 5)
divide(10, 2)
