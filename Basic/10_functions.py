# Functions

def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()


def sum_two_values(first_value: int, second_value: int):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
# sum_two_values("5", "7")
# sum_two_values(1.4, 5.2)


def sum_two_values_with_return(first_value: int, second_value: int):
    return (first_value + second_value)


my_result: int = sum_two_values_with_return(10, 5)
print(my_result)


def print_name(name: str, surname: str):
    print(f"{name} {surname}")


print_name(surname="Reyes", name="Andy")


def print_name_with_fefault(name: str, surname: str, alias: str = "Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_fefault("Andy", "Reyes")
print_name_with_fefault("Andy", "Reyes", "codeShadows")


def print_upper_texts(*texts: str):
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "Andy")
