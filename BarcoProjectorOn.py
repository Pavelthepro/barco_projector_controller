#!/usr/bin/python3

import requests
import re
import time
import sys
import json

def main():
  leftscreen = 'http://192.168.1.6'
  rightscreen = 'http://192.168.1.4'
  backscreen = 'http://192.168.1.5'
  # projectorAddress = 'http://192.168.1.87'
  # username = 'EPSONWEB'
  # password = 'admin'

  # auth = requests.auth.HTTPBasicAuth(username, password)
  # headers= {'Referer': projectorAddress + '/cgi-bin/webconf'}
  result = getRequest(leftscreen + '/BcSrcGen.htm')
  #print (result.text)
  
  # Changing Video Source
  headers = {
        "Host" : "192.168.1.6",
        "Connection" : "keep-alive",
        "Content-Length" : "27",
        "Pragma" : "no-cache",
        "Cache-Control" : "no-cache",
        "Origin" : "http://192.168.1.6",
        "Upgrade-Insecure-Requests" : "1",
        "Content-Type" : "application/x-www-form-urlencoded",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer" : "http://192.168.1.6/tgi/BcSrcGen.tgi",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "en-US,en;q=0.9,uk;q=0.8"
  }
  payload = {'itemName' : 'pwrchg', 'itemValue' : 1}
  r = requests.post( leftscreen + '/tgi/BcSrcGen.tgi', headers=headers, data=payload )

  print(r)

def getRequest(url):
    return requests.get(url)


if __name__ == '__main__':
  main()
# def postRequest(url, data):
#   return requests.post(projectorAddress + url, data = data, auth = auth,
#                        headers = headers)

# def projectorIsOn():
#   r = postRequest('/cgi-bin/webconf', {'page': '05'}) # Get info page
#   retval = r.text.find('The projector is currently on standby.<BR>') == -1
#   print(retval)
#   return retval

# def turnProjectorOn():
#   if not projectorIsOn():
#     getRequest('/cgi-bin/directsend?KEY=3B')

# def turnProjectorOff():
#   if projectorIsOn():
#     getRequest('/cgi-bin/directsend?KEY=3B')
#     time.sleep(0.3)
#     getRequest('/cgi-bin/directsend?KEY=3B')

# argument = sys.argv[1] or ''
# if sys.argv[1] == 'on':
#   turnProjectorOn()
# elif sys.argv[1] == 'off':
#   turnProjectorOff()
# else:
#   print('Run script with parameter 'on' or 'off'')
#   sys.exit(1)

# sys.exit(0)
