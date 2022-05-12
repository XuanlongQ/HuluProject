#!/usr/bin/python
import requests
import json
from logging import exception

# local package
from log import Logger 
from toolFunc import ParseWork


# get results content
def getResults(results):
    for result in results:
        id = ParseWork.getId(result)
        publication_year = ParseWork.getPublicationYear(result)
        firstauthor,institutions_author,countrycode_author = ParseWork.getFirstAuthor_Institution_Countrycode(result)
        cited_by_api_url = ParseWork.getCitedByApiUrl(result)
        abstract = ParseWork.getAbstract(result)
        print(id,publication_year,institutions_author,countrycode_author,cited_by_api_url)  
        print(abstract)  
        break
    

# get the request from cursorpage 
def getResponse(url):
    """_summary_

    Args:
        url (str): the content you wanna get from work

    Returns:
        str,json: cur is next cursor, results is the result of this work
    """
    resp = requests.get(url).json()
    print(resp["meta"])
    
    cur = resp["meta"]["next_cursor"]
    results = resp["results"]
    return cur,results

# result to files
def writeResq(res):
    """write json to file 

    Args:
        res (None): no return value
    """
    try:
        with open("pro/experimentdata/test1.json","a+",encoding= "utf-8") as f:
            json.dump(res, f, indent=4)
            f.close()
    except Exception as e:
        print("write error:",e)
        Logger('pro/logdata/error.log', level='error').logger.error(e)
    

if __name__ == '__main__':
    
    urls = []
    log = Logger('pro/logdata/all.log',level='debug')
    #Logger('pro/logdata/error.log', level='error').logger.error('content')
    for url in urls:
        pass
    
    url = "https://api.openalex.org/works?mailto=zd675589296@qq.com&per-page=10&filter=publication_year:2020,institutions.ror:https://ror.org/042nb2s44&cursor="
    
    """
    # Add the mailto=you@example.com parameter in your API request, like this: https://api.openalex.org/works?mailto=you@example.com
	# Use polite pool
    BASE_URL = "https://api.openalex.org"
    MAIL_ADDRESS = "mailto=zd675589296@qq.com"
    PER_PAGE = "10"
    INSTITUTION = "institutions.ror:https://ror.org/042nb2s44"
    testUrl = BASE_URL + "/works?" + MAIL_ADDRESS + "&per-page=" + PER_PAGE + "&filter=publication_year:2020," + INSTITUTION + "&cursor="
    print(testUrl)
    """

    # 计数页
    count = 0
    cur = "*"
    # writeResq(res)
    while cur:
        count = count + 1
        print(count)
        newUrl = url + cur
        print("url is :",newUrl)
        cur,results = getResponse(newUrl)
        
        getResults(results)
        
        # print(cur,type(cur))
        # writeResq(results) 
        break
        

        
    

