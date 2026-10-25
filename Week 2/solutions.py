def get_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [float(num) for num in data]

def calc_mean(numbers):
    return sum(numbers) / len(numbers)

def print_result(mean):
    print(f"The average of the numbers is: {mean}")

def ask_filename():
    return input("Enter the name of the file to load data from: ")


if __name__ == "__main__":
    filename = ask_filename()
    try:
        numbers = get_data(filename)
        mean = calc_mean(numbers)
        print_result(mean)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains non-numeric values.")
    except ZeroDivisionError:
        print("Error: The file is empty, cannot calculate mean.")

