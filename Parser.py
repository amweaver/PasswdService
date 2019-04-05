import typing

# are there fields that should always be filled, so I should error check them?
def passwdParser(lines) -> typing.List:
    elements = []
    for line in lines:
        print(line)
        values = line.split(":")
        print(values) # size of values should always be 7
        entry = {"name": values[0], "uid": values[2], "gid": values[3],
                 "comment": values[4], "home": values[5], "shell": values[6]} # there has to be a better way to parse this
        elements.append(entry) # is there a way I can order it like it is in the specification?
    return elements

# members must be separated by commas, and I must make them a list
def groupParser(lines) -> typing.List:
    elements = []
    for line in lines:
        print(line)
        values = line.split(":")
        print(values) # values should be 4
        entry = {"name": values[0], "gid": values[2], "members": values[3].split(",")} # there has to be a better way to parse this
        elements.append(entry) # is there a way I can order it like it is in the specification?
    return elements

