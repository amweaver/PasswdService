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

# this is for the nonbasic/nonquery cases
def GetContentsSpecial(pathtousers, pathtogroups, requestpath) -> typing.List:
    if os.stat(pathtousers).st_size == 0 or os.stat(pathtogroups).st_size == 0:
        return ['error: path file is empty. Users: contact server administrator about this issue']
    uid = requestpath.replace("/users/", '')
    uid = uid.replace("/groups", '')
    if not uid.isdigit():
        return ['error: invalid uid provided']
    lookup = dict([("uid", uid)])
    file_object = open(pathtousers, "r")
    lines = passwdParser(file_object, lookup)
    if len(lines) != 1:
        return ['error: uid found multiple times']
    lookup['members'] = [lines[0]['name']]
    del lookup["uid"] # otherwise, groups will look for the uid field
    file_object = open(pathtogroups, "r")
    return groupParser(file_object, lookup)

