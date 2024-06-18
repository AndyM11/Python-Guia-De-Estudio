# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_string_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))  # Longitud de la cadena

# Variables en una sola linea
name, surname, alias, age = "Juan", "Perez", "JP", 30
print("Me llamo:", name, surname, "mi edad es:", age, "Y mi alias es:", alias)

# Inputs
# first_name = input("¿Cual es tu nombre?: ")
# edad = input("¿Cual es tu edad?:")

# print("Hola", first_name, "tu edad es", edad, "años")

# Cambio de tipo de dato
# name = 35
# age = "Juan"
# print(name)
# print(age)

# ¿Forzamos el tipo de dato?
# address: str = "Mi direccion"
# address = True
# address = 5
# address = 1.2
# print(type(address))
