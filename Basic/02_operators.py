from prettytable import PrettyTable
# Opeadores Aritméticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)

print("Hola" + "Python")
print("Hola" + str(10))
print("Hola\n" * 5)

# Operadores Comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(4 == 4)
print(3 != 4)
print("\n")

# Operadores Lógicos

print(3 > 4 and ("Hola" > "Python"))
print(3 > 4 or ("Hola" > "Python"))
print(not (3 > 4))
print("\n")


# Table de verdad

# Definir los valores de verdad
valores = [False, True]

# Crear una tabla bonita
tabla = PrettyTable(['A', 'B', 'A AND B'])

# Llenar la tabla con los valores de verdad
for a in valores:
    for b in valores:
        tabla.add_row([a, b, a and b])

# Imprimir la tabla
print(tabla)
