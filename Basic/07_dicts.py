#  Dictionaries

my_dict: dict = {}
my_other_dict: dict = dict()

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "Edad": 30,
    1: "Python",
}

my_dict = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "Edad": 30,
    "Lenguajes": {"Python", "JaveScript", "Swift"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Av. Siempre Viva"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Juan" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = my_other_dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = my_other_dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = my_other_dict.fromkeys(my_dict, "MoureDev")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
