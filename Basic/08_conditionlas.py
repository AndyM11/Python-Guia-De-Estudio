# Conditionals

my_condition = False

if my_condition:  # Es lo mismo que if my_conditional = True:
    print("Se ejecuta la condicion del if")

my_condition: int = (5 * 5)

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")

elif my_condition == 25:
    print("Es igual a 25")

else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto que 25")


print("La ejecución continua")


my_string = ""

if not my_string:
    print("Mi cadena de texto esta vacia")
else:
    print("Mi cadena de texto es vacia")

if my_string == "Mi cadena de texto":
    print("Estas cadenas de texto coinciden")
