import os
from Parser import passwdParser
from Parser import groupParser
import RequestHandler
import requests
import threading

t = threading.Thread(target=RequestHandler.runHTTPService)
t.start()

'''r = requests.get('http://localhost:8000/users')
print(r.text)
r = requests.get('http://localhost:8000/groups')
print(r.text)

r = requests.get('http://localhost:8000/users/query%3Fname=root')
print(r.text)
r = requests.get('http://localhost:8000/groups/query%3Fmember=root&member=bin')
print(r.text)'''

r = requests.get('http://localhost:8000/users/3')
print(r.text)
r = requests.get('http://localhost:8000/groups/30')
print(r.text)
r = requests.get('http://localhost:8000/users/201/groups')
print(r.text)

RequestHandler.stopHTTPService()
