import typing

# are there fields that should always be filled, so I should error check them?


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
    if not line[0].isalnum() or len(line[0]) > 32 or len(line[0]) < 0 or (line[0].isdigit()):  # check that user is actually valid
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

    return True

# members must be separated by commas, and I must make them a list
def groupParser(lines) -> typing.List:
    elements = []
    for line in lines:
        values = line.split(":")
        #print(values) # values should be 4
        if len(values) != 4:
            print("Invalid entry detected. Skipping.")
        entry = {"name": values[0], "gid": values[2], "members": values[3].split(",")} # there has to be a better way to parse this
        elements.append(entry) # is there a way I can order it like it is in the specification?
    return elements

