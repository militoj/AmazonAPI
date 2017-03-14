# borrowed from http://code.runnable.com/UqqYPSGIpqAeAAPc/how-to-use-restful-api-with-requests-for-python


import requests
import json
import restful_webapi
import os

restful_webapi.run_server()

service = 'http://localhost:8080'

print ("Creating the message...")
created = None
data = json.dumps("Hello world")
r = requests.post(service, data=data)
created = r.json()['created']
print ("Message ID: " + str(created))

print ("Showing the message...")
r = requests.get(service + '/' + str(created))
print ("Service returned: " + str(r.json()))

print ("Updating the message...")
data = json.dumps("Welcome, world")
r = requests.put(service + '/' + str(created), data=data)
print ("Service returned: " + str(r.json()))

print ("Showing the message again...")
r = requests.get(service + '/' + str(created))
print ("Service returned: " + str(r.json()))

print ("Deleting the message...")
r = requests.delete(service + '/' + str(created))
print ("Service returned: " + str(r.json()))

# Stop the server and quit
os._exit(0)
