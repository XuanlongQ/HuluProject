#!/usr/bin/python
import requests
import json


# local package
# from log import Logger 
from toolFunc import ParseWork

"""
Get information from api url
Many items were parsed by a api_url
"""
#log = Logger('pro/logdata/all.log',level='debug')



def chooseMethod(result,method = 1):
    """choose the subject by which method,default use top level

    Args:
        method (int, optional): _description_. Defaults to 1.
        result(json): response from url
    Returns:
        str: the method and its concept
    """
    if method == 1:
        # method 1 - find the most top level concept 
        return ParseWork.findTopLevel(result)
    else:
        # method 2 - find the highest score concept 
        return ParseWork.findHighestScoreConcept(result)

def parseCitedByApiUrl(cited_by_api_url):
    """ Use to get the cited papers' id and subject

    Args:
        cited_by_api_url (str): url of the cited paper api

    Returns:
        str: these papers' id and subject
    """
    referencePaperSubject = {}
    
    try:
        respdata = requests.get(cited_by_api_url)
        resp = respdata.json()
        #log.logger.info("get cited_by_api_url papaers' id, papers' subject.")
        results = resp["results"]
        for result in results:
            id = result["id"] # str
            # choose Method 1 default
            conceptValue = chooseMethod(result,1)
            referencePaperSubject[id] = conceptValue  # choose your method
            
        # print(referencePaperSubject) # get the dict of different id for their subject
        #  print(meta,type(meta))
        # print(results,type(results))
    
        # log.logger.info("return papers' id,subject,type dict.")
        return referencePaperSubject # top level, str
    except Exception as e:
        print("parse cited url error:",e)
        # Logger('pro/logdata/error.log', level='error').logger.error(e) 
    

    

# this package use to parse cited_by_api_url
# cited_by_api_url = "https://api.openalex.org/works?filter=cites:W2939308062"
# z = parseCitedByApiUrl(cited_by_api_url)
# print(z)

