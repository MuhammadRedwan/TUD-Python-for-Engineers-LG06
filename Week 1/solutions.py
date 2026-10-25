# 1
print("Hello, world!")

# 2
value = True
print(value, type(value))

# 3
list1 = [1, 2, 3] # List equivalent to an an array in other languages
tuple1 = (1, 2, 3) # Tuple is immutable
dict1 = {"a": 1, "b": 2, "c": 3} # Dictionary with key-value pairs

# 4 
from ipydex import IPS
IPS() # This will open an interactive shell in the middle of the code execution

# 5
from ipydex import activate_ips_on_exception
activate_ips_on_exception() # This will open an interactive shell when an exception occurs e.g. dividing by zero
a = 1, b = 0
c = a / b # This will raise a ZeroDivisionError and open an interactive shell

# 6
print(len(list1)) # Length of the list
print(len(tuple1)) # Length of the tuple
print(len(dict1)) # Length of the dictionary (number of key-value pairs)

for item in list1:
    print(item)

for item in tuple1:
    print(item)

for key, value in dict1.items():
    print(key, value)

# 7
# The following code might be prone to errors, as user might input non-numeric values such as strings. 
x = float(input("Enter the first number: "))
if not (-10 <= x <= 10):
    print("The first number is not in the interval [-10, 10].")
y = float(input("Enter the second number: "))
if not (-10 <= y <= 10):
    print("The second number is not in the interval [-10, 10].")

# 8

print("The sum of the two numbers is:", x + y)
print("The mean of the two numbers is:", (x + y) / 2)


# 9
N =  5 # example for a positive integer
numbers = []
for i in range(N):
    num = float(input(f"Enter number {i + 1}: "))
    if not (-10 <= num <= 10):
        print(f"The number {num} is not in the interval [-10, 10].")
    numbers.append(num)

print("The sum of the numbers is:", sum(numbers))
print("The mean of the numbers is:", sum(numbers) / len(numbers))