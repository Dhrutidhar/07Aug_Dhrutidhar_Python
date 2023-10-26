# Q 20.) Write python program that user to enter only odd numbers, else will raise an exception.


try:
    user_input = int(input("Enter an odd number: "))

    if user_input % 2 == 0:
        raise ValueError("Entered number is even, Please enter an odd number.")

    print("You entered an odd number:", user_input)

except Exception as e:
    print(f"Error: {e}")

finally:
    print("Finally will be executed!!!!!")
