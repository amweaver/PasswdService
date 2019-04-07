import os
import typing
from Parser import queryRegex
from Parser import passwdParser
from Parser import groupParser

def GetContents(pathtofile, path) -> typing.List:
    lines = []
    with open(pathtofile, "r") as file_object:
        for line in file_object:
            if line.strip() != "":
                lines.append(line.rstrip())
    if path.startswith('/users'):
        query = queryRegex(path)
        ##print(query)
        return passwdParser(lines, query)
    if path.startswith('/groups'):
        query = queryRegex(path)
        ##print(query)
        return groupParser(lines, query)
    else:
        return ['error: invalid request /users and /groups are the only accepted queries']
