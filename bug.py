def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list) #this will return 0, which is correct behavior. 
print(f"The average is: {average}")

my_list = [1,2,3,4,5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [1,2,'a',4,5]
average = calculate_average(my_list) #this will throw TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(f"The average is: {average}")