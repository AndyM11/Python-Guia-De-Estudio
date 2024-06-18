#  File Handling

#  .txt file

# import xml
import csv
import json
txt_file = open("Intermediate/my_file.txt", "w+",
                encoding="utf-8")  # Escritura y lectura
txt_file.write("Mi nombre es Andy\n"
               "Mi apellido es Reyes\n"
               "25 Años\n"
               "Y mi lenguaje de programación preferido es JavaScript")
# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta Python")
print(txt_file.readline())
txt_file.close()

# import os
# os.remove("Intermediate/my_file.txt")

#  .json file

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Andy",
    "surname": "Reyes",
    "age": 25,
    "language": ["JavaScript", "Python", "Java", "C++"],
    "website": "https://andyreyes.dev"
}

json.dump(json_test, json_file, indent=2)
json_file.close()

with open("Intermediate/my_file.json", "r") as json_other_file:
    for line in json_other_file.readlines():
        print(line)
json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])


# .csv file

with open("Intermediate/my_file.csv", "w+", encoding="utf8") as csv_file:
    csv_write = csv.writer(csv_file)
    csv_write.writerow(["name", "surname", "age", "language", "website"])
    csv_write.writerow(
        ["Andy", "Reyes", 25, "JavaScript", "https://andyreyes.dev"])
    csv_write.writerow(["Roswell", "", 2, "COBOL", ""])
csv_file.close()

with open("Intermediate/my_file.csv", encoding="utf8") as my_other_csv:
    for line in my_other_csv.readlines():
        print(line)

# .xlsx file
# import xlrd # pip install xlrd # debe instalarse el modulo

# .xml file
