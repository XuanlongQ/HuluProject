#!/usr/bin/python
import requests
import json
from logging import exception

# local package
from log import Logger
from toolFunc import ParseAuthor, ParseWork
from parseUrl import parseCitedByApiUrl
from DoInterdisplinaryWork import getDisplineWork


# get results content
def  getResultsWork(results):
    """Get entities of work

    Args:
        results (strs): it depends on the number of we want return,need to be improved
    """
    for result in results:
        id = ParseWork.getId(result)
        publication_year = ParseWork.getPublicationYear(result)
        firstauthor,institutions_author,countrycode_author = ParseWork.getFirstAuthor_Institution_Countrycode(result)
        cited_by_api_url = ParseWork.getCitedByApiUrl(result)
        abstract = ParseWork.getAbstract(result)
        print(id,publication_year,institutions_author,countrycode_author,cited_by_api_url)  
        print(abstract)  
        print(firstauthor)
        
        subject = parseCitedByApiUrl(cited_by_api_url)
        print(subject)
        
        break
    
def getResultsAuthor(results):
    """Get entities of author

    Args:
        results (restlt): list of x_concepts

    Returns:
        dict: {authorid:subject}
    """
    AuthorConcepts = {}
    for result in results:
        authorId,authorConcept = ParseAuthor.getResultsAuthor(result)
        AuthorConcepts[authorId] = authorConcept
        print(AuthorConcepts)
    return AuthorConcepts
        

# get the request from cursorpage 
def getResponseWork(workUrl):
    """_summary_

    Args:
        url (str): the content you wanna get from work

    Returns:
        str,json: cur is next cursor, results is the result of this work
    """
    resp = requests.get(workUrl).json()
    print(resp["meta"])
    
    cur = resp["meta"]["next_cursor"]
    resultsWork = resp["results"]
    return cur,resultsWork


def getResponseAuthor(AuthorIdUrl):
    """Get response from authorid url

    Args:
        AuthorIdUrl (str): authorid url

    Returns:
        list: list of x_concepts
    """
    resp = requests.get(AuthorIdUrl).json()
    print(resp["x_concepts"],type(resp["x_concepts"]))
    resultsAuthor = resp["x_concepts"]
    return resultsAuthor
    

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
        
        ####################################         Work Part         ###################################
        workUrl = url + cur
        print("url is :",workUrl)
        cur,resultsWork = getResponseWork(workUrl)
        # getResultsWork(resultsWork)
        getDisplineWork(resultsWork)
        
        
        ####################################         Author Part         ###################################
        # AuthorIdUrl = "https://api.openalex.org/authors/A2903904671" 
        # resultsAuthor = getResponseAuthor(AuthorIdUrl)
        # AuthorConcepts = getResultsAuthor(resultsAuthor)
        
        
        ####################################         other Parts         ###################################

        # print(cur,type(cur))
        # writeResq(results) 
        break
        

        
    

