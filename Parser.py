import typing

def passwdParser(lines) -> typing.List:
    elements = []
    for line in lines:
        #print(line)
        values = line.split(":")
        #print(values)
        if passwdValidate(values):
            entry = {"name": values[0], "uid": values[2], "gid": values[3],
                    "comment": values[4], "home": values[5], "shell": values[6]}  # there has to be a better way to parse this
            elements.append(entry)  # is there a way I can order it like it is in the specification?
    return elements

def passwdValidate(line) -> bool:
    if len(line) != 7:
        print("Invalid number of fields for a passwd entry")
        return False
    if (not line[0]) or (not line[0].isalnum()) or len(line[0]) > 32 or line[0].isdigit():  # check that user is actually valid
        print("User field is not valid")
        return False
    if (not line[2].isdigit()) or int(line[2]) < 0:  # POSIX reserves -1 for an omitted argument. Should I still remove it?
        print("uid must be a positive number")
        return False
    if int(line[2]) > 4294967295:
        print("uid must not exceed 4,294,967,295")
        return False
    if line[2] == '0' and line[0] != "root":
        print("Only root is allowed to have uid 0")
        return False
    if (not line[3].isdigit()) or int(line[3]) < 0:  # POSIX reserves -1 for an omitted argument. Should I still remove it?
        print("gid must be a positive number")
        return False
    if int(line[3]) > 4294967295:
        print("gid must not exceed 4,294,967,295")
        return False
    # there are no constraints on the comment, so we do not need to check it
    if not line[5].startswith('/'): # this also covers the case that it is an empty string
        print("Home is not an absolute path")
        return False
    if line[6] and not line[6].startswith('/'):
        print("Shell must be an absolute path if present")
        return False
    return True

# members must be separated by commas, and I must make them a list
def groupParser(lines) -> typing.List:
    elements = []
    for line in lines:
        values = line.split(":")
        #print(values)
        if groupValidate(values):
            entry = {"name": values[0], "gid": values[2], "members": values[3].split(",")} # there has to be a better way to parse this
            elements.append(entry) # is there a way I can order it like it is in the specification?
    return elements

def groupValidate(line) -> bool:
    if len(line) != 4:
        print("Invalid number of fields for a group entry")
        return False
    if (not line[0]) or len(line[0]) > 32 or line[0].isdigit():  # check that group is actually valid
        print("Group field is not valid")
        return False
    if (not line[2].isdigit()) or int(line[2]) < 0:  # POSIX reserves -1 for an omitted argument. Should I still remove it?
        print("uid must be a positive number")
        return False
    if int(line[2]) > 4294967295:
        print("uid must not exceed 4,294,967,295")
        return False
    members = line[3].split(',')
    for member in members:
        member = member.strip()
        if member and ((not member.isalnum()) or len(member) > 32 or member.isdigit()):  # check that user is actually valid
            print("User field is not valid")
            print(member)
            return False
    return True
