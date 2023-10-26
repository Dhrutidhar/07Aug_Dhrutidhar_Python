# Q 19.) How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.


try:
    num_str = input("Enter a number: ")
    num = int(num_str)
    result = 10 / num
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("No exceptions occurred.")

finally:
    print("This will be executed no matter try except runs.")
