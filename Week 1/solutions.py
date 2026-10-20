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
x = 1, y = 0
z = x / y # This will raise a ZeroDivisionError and open an interactive shell

# 6
print(len(list1)) # Length of the list
print(len(tuple1)) # Length of the tuple
print(len(dict1)) # Length of the dictionary (number of key-value pairs)