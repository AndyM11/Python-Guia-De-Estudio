# Tuples

my_tuple: tuple = tuple()
my_other_tuple: tuple[int, int, int]

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (60, 30, 90)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) # IndexError
# print(my_tuple[-6]) # IndexError

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


# print(my_sum_tuple[3, 6]) TypeError: tuple indices must be integers or slices, not tuple.
print(my_sum_tuple[3:6])

my_list = list(my_tuple)  # Convert tuple to list.
print(type(my_list))

my_list[4] = "MoureDev"
my_list.insert(1, "Azul")
print(my_list)

my_tuple = tuple(my_list)  # Convert list to tuple
print(my_tuple)

# del my_tuple[2]  # TypeError: 'tuple' object doesn't support item deletion.

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined.
