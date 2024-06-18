# Sets

my_sets: set = set()
my_other_sets: set = {1, 2, 3}

print(type(my_sets))
print(type(my_other_sets))  # Inicialmente es un diccionario

my_other_sets = {"Brais", "Moure", 35}
print(my_other_sets)

print(len(my_other_sets))

# print(my_other_sets[0])  # No se puede acceder a los elementos por índice

my_other_sets.add("MoureDev")
print(my_other_sets)  # Un set no es una estructura ordenada

my_other_sets.add("MoureDev")  # Un set no permite elementos duplicados
print(my_other_sets)

print("Moure" in my_other_sets)
print("Mouri" in my_other_sets)

my_other_sets.remove("Moure")
print(my_other_sets)

my_other_sets.clear()
print(len(my_other_sets))

del my_other_sets
# print(my_other_sets)  # NameError: name 'my_other_sets' is not defined

my_sets = {"Brais", "Moure", 35}
my_list = list(my_sets)
print(my_list)

my_other_sets = {"Kotlin", "Java", "Python", "Swift", "JavaScript", "C#"}
my_new_set = my_sets.union(my_other_sets)
print(my_new_set)

print(my_new_set.difference(my_sets))
