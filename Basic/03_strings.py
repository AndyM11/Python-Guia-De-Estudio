# Strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
print(my_string.upper())
print(my_string.lower())

my_new_line_string = "Este es un String\ncon un salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con un tabulacion"
print(my_tab_string)

my_scaped_string = "Este es un String con una comilla simple \' \n"
print(my_scaped_string)

# Formateo

name, surname, age = "Andy", "Reyes", 25
print("Mi nombre es {}, mi apellido es {} y tengo {} years"
      .format(name, surname, age))

print(f"Mi nombre es {name}, mi apellido es {surname} y tengo {age} years")


# Deseempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reverse_language = language[::-1]
print(reverse_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count('t'))
print(language.find('t'))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())
print(language.startswith('py'))
