import os
import typing
from Parser import passwdParser
from Parser import groupParser

def GetContents(pathtofile, path) -> typing.List:
    lines = []
    with open(pathtofile, "r") as file_object:
        for line in file_object:
            if line.strip() != "":
                lines.append(line.strip())
    if path.startswith('/users'):
        return passwdParser(lines)
    if path.startswith('/groups'):
        return groupParser(lines)
    else:
        return ['error: invalid request /users and /groups are the only accepted queries']
