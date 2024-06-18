# Exception Handling

number_one = 5
number_two = 1
number_one = "1"

try:
    print(number_one + number_two)
    print("No se ha producido un error.")
except TypeError:
    # Se ejecuta si se produce una excepción.
    print("Se ha producido un error.")
else:  # Opcional.
    # Se ejecuta sino se produce una excepción.
    print("La ejecución continúa correctamente.")
finally:  # Opcional.
    # Se ejecuta siempre.
    print("La ejecución continúa.")

# Exceptiones por tipo
try:
    print(number_one + number_two)
    print("No se ha producido un error.")
# except TypeError as e:
#     print("Se ha producido un TypeError: " + str(e))
# except ValueError:
#     print("Se ha producido un ValueError.")
except Exception as error:  # No recomendado, pero funcional.
    print(error)
