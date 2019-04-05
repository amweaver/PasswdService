import os
from Parser import passwdParser
from Parser import groupParser
import RequestHandler
import requests
import threading

t = threading.Thread(target=RequestHandler.runHTTPService)
t.start()

r = requests.get('http://localhost:8000/users')
print(r.text)
r = requests.get('http://localhost:8000/groups')
print(r.text)

RequestHandler.stopHTTPService()
