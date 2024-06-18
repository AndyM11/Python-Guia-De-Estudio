#  Regular Expressions
import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# match
match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])


match = re.match("Esta no es la lección", my_other_string)
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))


# search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

#  findall

findall = re.findall("lección", my_string, re.I)
print(findall)

#  split
print(re.split(":", my_string))

#  sub
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Patterns

pattern = r"[l|L]ección"
print(re.findall(pattern, my_string))

pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

# email validation regular expression
pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z-.]+$"
print(re.findall(pattern, "correo@corre.com.do"))
