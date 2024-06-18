# Loops

#  While

my_condition: int = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
# if my_condition == 10:
#     print("Mi condición es igual a 10")
# elif my_condition == 10:
# print("Mi condición es igual a 10") SyntaxError: invalid syntax
else:
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")


# For
my_list = [35, 24, 62, 52, 30, 17]
for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
for element in my_tuple:
    print(element)

my_sets = {"Brais", "Moure", 35}
for element in my_sets:
    print(element)

my_dict = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "Edad": 30,
    1: "Python",
}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("Ek bucle for a finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    else:
        print("Se ejecuta")
else:
    print("Ek bucle for a finalizado")
