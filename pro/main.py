#!/usr/bin/python
from logging import exception
import requests
import json
from log import Logger 

# private package



# get results content
def getResults(resp):
    # print(type(resp))
    results = resp["results"]
    for result in results:
        id = result["id"]  # unique paper ID, str
        publication_year = result["publication_year"] # year of pub,int
        authorships = result["authorships"] # all the authors' information,list
        firstauthor = [x for x in authorships][0] # authors - first author,dict - add test cases
        institutions_author = firstauthor["raw_affiliation_string"] # institutions of first author,str
        countrycode_author = firstauthor["institutions"][0]["country_code"] # country code of first author,str
        
        
        cited_by_api_url = result["cited_by_api_url"] # references cited in the data

        # print(id,type(id))
        # print(publication_year,type(publication_year))
        # print(authorships[0],type(authorships[0]))
        # print(institutions_author,type(institutions_author))
    
        # print(countrycode_author,type(countrycode_author))
        # print(cited_by_api_url,type(cited_by_api_url))
        
        break
    return cited_by_api_url
    
    print(len(results))
    


# get the request from cursorpage 
def getResponse(url):
    resp = requests.get(url).json()
    
    # get result
    cited_by_api_url = getResults(resp)
    
    
    # output resps' meta info
    print(resp["meta"])
    
    cur = resp["meta"]["next_cursor"]
    results = resp["results"]
    
    return cur,results,cited_by_api_url

# result to files
def writeResq(res):
    try:
        with open("pro/experimentdata/test1.json","a+",encoding= "utf-8") as f:
            json.dump(res, f, indent=4)
            f.close()
    except Exception as e:
        print("write error:",e)
        Logger('pro/logdata/error.log', level='error').logger.error(e)
    

if __name__ == '__main__':
    
    log = Logger('pro/logdata/all.log',level='debug')
    #Logger('pro/logdata/error.log', level='error').logger.error('content')
    
   
    # Add the mailto=you@example.com parameter in your API request, like this: https://api.openalex.org/works?mailto=you@example.com
	# Use polite pool
    BASE_URL = "https://api.openalex.org"
    MAIL_ADDRESS = "mailto=zd675589296@qq.com"
    PER_PAGE = "10"
    INSTITUTION = "institutions.ror:https://ror.org/042nb2s44"
    
    # test url - need to be updated to yaml
	# https://api.openalex.org/works?filter=institutions.ror:https://ror.org/02y3ad647
    testUrl = BASE_URL + "/works?" + MAIL_ADDRESS + "&per-page=" + PER_PAGE + "&filter=publication_year:2020," + INSTITUTION + "&cursor="
    # print(testUrl)
    
    # 计数页
    count = 0

    cur = "*"
    # writeResq(res)
    while cur:
        count = count + 1
        print(count)
        
        newUrl = testUrl + cur
        print("url is :",newUrl)
        
        # cur,results,cited_by_api_url = getResponse(newUrl)
        # print(cur)
        # writeResq(results) 
        
        # print(cited_by_api_url)
        break
        

        
    

