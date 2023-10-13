# Q 14.) Write a Python program to find the second smallest number in a list.


my_numbers = [5, 2, 8, 1, 3, 9, 4, 6]

my_numbers.sort()

print(my_numbers)
print(my_numbers[1])


"""if len(my_numbers) > 2:
    smallest = float("inf")  # Positive infinity as initial value
    second_smallest = float("inf")
    for num in my_numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    print("List:", my_numbers)
    print("Second smallest number:", second_smallest)

else:
    print("List should have at least two elements.")"""