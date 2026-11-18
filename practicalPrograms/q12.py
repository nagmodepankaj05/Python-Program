try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    c = a / b
    print("Division =", c)

except ValueError:
    print("Error: Please enter only integer values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("Error:", e)

finally:
    print("Program completed.")
