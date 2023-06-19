# Take input from the user and store it in a list
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Calculate the sum of all the elements in the list
sum_of_numbers = sum(numbers)
print("Sum of numbers:", sum_of_numbers)

# Find the smallest number
smallest_number = min(numbers)
print("Smallest number:", smallest_number)

# Find the largest number
largest_number = max(numbers)
print("Largest number:", largest_number)

# Display the list in ascending order
ascending_order = sorted(numbers)
print("List in ascending order:", ascending_order)

# Display the list in descending order
descending_order = sorted(numbers, reverse=True)
print("List in descending order:", descending_order)

# Convert the list into a tuple
numbers_tuple = tuple(numbers)
print("List converted to tuple:", numbers_tuple)

# Delete the list
del numbers
print("List deleted")
