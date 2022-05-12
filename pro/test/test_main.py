#!/usr/bin/python
import requests
import json

from pro.toolFunc import ParseWork


url = "https://api.openalex.org/works?mailto=zd675589296@qq.com&per-page=10&filter=publication_year:2020,institutions.ror:https://ror.org/042nb2s44&cursor=*"

resp = requests.get(url).json()

results = resp["results"]

a = ParseWork.getAbstract(results)

print(a)

# for result in results:
#     abstract_inverted_index = result["abstract_inverted_index"]
#     str = " "
#     seq = [ _ for _ in abstract_inverted_index.keys() ] # abstract list
#     abstract = str.join(seq) # abstract str
#     print(abstract,type(abstract))   
#     break



# # BASE_URL = "https://api.openalex.org"
# # MAIL_ADDRESS = "mailto=zd675589296@qq.com"
# # PER_PAGE = "10"
# INSTITUTION = "institutions.ror:https://ror.org/042nb2s44"

# # # test url - need to be updated to yaml
# # # https://api.openalex.org/works?filter=institutions.ror:https://ror.org/02y3ad647
# # testUrl = BASE_URL + "/works?" + MAIL_ADDRESS + "&per-page=" + PER_PAGE + "&filter=publication_year:2020," + INSTITUTION + "&cursor="
# # # print(testUrl)

# def getResponse(url):
#     resp2 = requests.get(url)
#     print(resp2)
#     resp =  requests.get(url).json()
    
#     # output resps' meta info
#     print(resp["meta"])


# baseUrl = "https://api.openalex.org"

# payload = {
#     "mailto": "zd675589296@qq.com",
#     "per-page": "10"
# }

# query_string = urllib.parse.urlencode(payload)
# print(query_string)
# url = baseUrl + "/works?"+query_string+"&filter=publication_year:2020,"+ INSTITUTION + "&cursor=*"
# print(url)
# gen = unquote(url)
# print(gen)

# getResponse(gen)



# # https://api.openalex.org/work?mailto=zd675589296@qq.com&per-page=10&filter=publication_year:2020,institutions.ror:https://ror.org/042nb2s44&cursor=*

# # https://api.openalex.org/works?mailto=zd675589296@qq.com&per-page=10&filter=publication_year:2020,institutions.ror:https://ror.org/042nb2s44&cursor=*




# # getResponse(url1)


