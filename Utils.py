import typing

def regexFix(dict) -> typing.Dict:
    fixedDict = {}
    for entry in dict:
        if dict[entry] != None:
            key = dict[entry].lstrip('&')
            key = key.replace(entry + '=', '')
            members = key.split('&')
            if len(members) == 1:
                if entry == 'member':
                    entry = 'members'
                fixedDict[entry] = members[0]
            else:
                if entry == 'member':
                    entry = 'members'
                fixedDict[entry] = members
    return fixedDict
