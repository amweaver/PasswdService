import os
import typing
from Parser import queryRegex
from Parser import passwdParser
from Parser import groupParser

def GetContents(pathtofile, requestpath) -> typing.List:
    lines = []
    if os.stat(pathtofile).st_size == 0:
        return ['error: path file is empty. Users: contact server administrator about this issue']
    with open(pathtofile, "r") as file_object:
        for line in file_object:
            if line.strip() != "":
                lines.append(line.rstrip())
    if requestpath.startswith('/users'):
        query = queryRegex(requestpath)
        ##print(query)
        return passwdParser(lines, query)
    if requestpath.startswith('/groups'):
        query = queryRegex(requestpath)
        ##print(query)
        return groupParser(lines, query)
    else:
        return ['error: invalid request /users and /groups are the only accepted queries']
