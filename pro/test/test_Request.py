# import requests

# url = "https://api.openalex.org/works?mailto=zd675589295@qq.com&per-page=50&filter=publication_year:2020,institutions.ror:https://ror.org/02kkvpp62&cursor="



# proxy = '202.55.5.209:8090' 
# proxies = {
#      'http': 'http://' + proxy
# }



# resp = requests.get(url,verify=False,proxies=proxies)
# print(resp.status_code,resp.json())  

from ast import Num
import re
a = "<http://ma-graph.org/property/level>"

# c ="<http://ma-graph.org/property/level>"
# b = a.rstrip(">").lstrip("<").split("/")[5]
# d = c.rstrip(">").lstrip("<").split("/")[4]
# print(d)
a = '<http://ma-graph.org/entity/417682> <http://xmlns.com/foaf/0.1/name> "Night air"^^<http://www.w3.org/2001/XMLSchema#string> .'

line = a.rstrip().split(" ",2)
specific_value = line[2]

name = specific_value.split("^^")[0].rstrip('"').lstrip('"')

print(name)