import os
from Parser import passwdParser
from Parser import groupParser

lines = []
with open(os.path.join("e:/Andrew Documents", "etcpasswd.txt"), "r") as file_object:
    for line in file_object:
        if line.strip() != "":
            lines.append(line.strip())
list = passwdParser(lines)
print(list)
print("Users parsed!")

lines = []
with open(os.path.join("e:/Andrew Documents", "etcgroup.txt"), "r") as file_object:
    for line in file_object:
        if line.strip() != "":
            lines.append(line.strip())
list = groupParser(lines)
print(list)
print("Groups parsed!")