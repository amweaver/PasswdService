import typing
import configparser
import os

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

def getUsers() -> str:
    config = configparser.ConfigParser()
    config.read('config.ini')
    userpath = config.get('Custom Paths', 'Custom User Path')
    if userpath != '' and userpath is not None and os.path.isfile(userpath):
        return userpath
    else:
        userpath = config.get('Default Paths', 'User Path')
        if userpath != '' and userpath is not None and os.path.isfile(userpath):
            return userpath
    return ''

def getGroups() -> str:
    config = configparser.ConfigParser()
    config.read('config.ini')
    grouppath = config.get('Custom Paths', 'Custom Group Path')
    if grouppath != '' and grouppath is not None and os.path.isfile(grouppath):
        return grouppath
    else:
        grouppath = config.get('Default Paths', 'Group Path')
        if grouppath != '' and grouppath is not None and os.path.isfile(grouppath):
            return grouppath
    return ''
