#!/usr/bin/python
import requests
import json
import urllib
# sys.path.append("..") 

# import urllib.parse
# url = 'https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?'

# data = {
#     'subscription-key':'2869a9d713e245af845f6272434cfb95',
#     'expr':'FC.FN=computer science',
# }

# query_string = urllib.parse.urlencode(data)
# print(query_string)
# url1 = url + '&'+query_string
# print(url1)

url = "https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?expr=Composite(AA.AuN=='jaime teevan')&count=2&subscription-key='2869a9d713e245af845f6272434cfb95'"

# endpoint= "https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?"
# expressionEqu = "Composite(FC.FId==40700)"
# subscribeKey = "&subscription-key=2869a9d713e245af845f6272434cfb95"

# url = endpoint + expressionEqu + subscribeKey

# 2869a9d713e245af845f6272434cfb95

import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '2869a9d713e245af845f6272434cfb95',
}

params = urllib.parse.urlencode({
    # Request parameters
    'model': 'latest',
    'count': '10',
    'offset': '0',
    'orderby': '{string}',
    'attributes': 'Id',
})

try:
    conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
    conn.request("GET", "/academic/v1.0/evaluate?expr={expr}&%s" % params, "Composite(AA.AuN=='jaime teevan')", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
