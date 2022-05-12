#!/usr/bin/python
import requests
import json


# local package
from log import Logger 
from toolFunc import FindConcept

"""
Get information from api url
Many items were parsed by a api_url
"""
log = Logger('pro/logdata/all.log',level='debug')



def chooseMethod(method = 1):
    """choose the subject by which method,default use top level

    Args:
        method (int, optional): _description_. Defaults to 1.

    Returns:
        func: the method
    """
    if method == 1:
        # method 1 - find the most top level concept 
        return FindConcept.findTopLevel
    else:
        # method 2 - find the highest score concept 
        return FindConcept.findHighestScoreConcept

def parseCitedByApiUrl(cited_by_api_url):
    """ Use to get the cited papers' id and subject

    Args:
        cited_by_api_url (str): url of the cited paper api

    Returns:
        str: these papers' id and subject
    """
    referencePaperSubject = {}
    
    resp = requests.get(cited_by_api_url).json()
    
    log.logger.info("get cited_by_api_url papaers' id, papers' subject.")
    
    meta = resp["meta"]  # - delete  
    results = resp["results"]
    
    for result in results:
        concepts = result["concepts"]
        id = result["id"] # str
        
        # choose Method 1 default
        chosenConcept = chooseMethod(1)
        conceptValue = chosenConcept(concepts)
        print(conceptValue)
        
        referencePaperSubject[id] = conceptValue  # choose your method
    # print(referencePaperSubject) # get the dict of different id for their subject
    #  print(meta,type(meta))
    # print(results,type(results))
    try:
        log.logger.info("return papers' id,subject,type dict.")
        return referencePaperSubject # top level, str
    except Exception as e:
        print("Return papers' id and suject error:",e)
        Logger('pro/logdata/error.log', level='error').logger.error(e) 
    

    

# this package use to parse cited_by_api_url
cited_by_api_url = "https://api.openalex.org/works?filter=cites:W2939308062"
z = parseCitedByApiUrl(cited_by_api_url)
print(z)

