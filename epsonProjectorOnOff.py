#!/usr/bin/python3

import requests
import re
import time
import sys

projectorAddress = 'http://192.168.1.87'
username = 'EPSONWEB'
password = 'admin'

auth = requests.auth.HTTPBasicAuth(username, password)
headers= {'Referer': projectorAddress + '/cgi-bin/webconf'}

def getRequest(url):
  return requests.get(projectorAddress + url, auth = auth, headers = headers)

def postRequest(url, data):
  return requests.post(projectorAddress + url, data = data, auth = auth,
                       headers = headers)

def projectorIsOn():
  r = postRequest('/cgi-bin/webconf', {'page': '05'}) # Get info page
  retval = r.text.find('The projector is currently on standby.<BR>') == -1
  print(retval)
  return retval

def turnProjectorOn():
  if not projectorIsOn():
    getRequest('/cgi-bin/directsend?KEY=3B')

def turnProjectorOff():
  if projectorIsOn():
    getRequest('/cgi-bin/directsend?KEY=3B')
    time.sleep(0.3)
    getRequest('/cgi-bin/directsend?KEY=3B')

argument = sys.argv[1] or ''
if sys.argv[1] == 'on':
  turnProjectorOn()
elif sys.argv[1] == 'off':
  turnProjectorOff()
else:
  print("Run script with parameter 'on' or 'off'")
  sys.exit(1)

sys.exit(0)
