#!/usr/bin/python

from toolFunc import ParseWork,writeResq
from parseUrl import chooseMethod,parseCitedByApiUrl


MIT = "https://ror.org/042nb2s44"
# Stanford = "https://ror.org/00f54p054"


def getDisplineWork(results):
    """Get one papers' subject and its cited papers' subjects

    Args:
        results (json):  content from responses' result
    
    Returns:
        dict: id,papers_concept,papers_citedconcepts
    """
    for result in results:
        global MIT
        institutions = ParseWork.getAuthorship(result) # get first author
        for institution in institutions:
            if institution["ror"] == MIT:
                displineWork = getPaper_citedConcptes(result)
                writeResq(displineWork)
            else:
                continue
            
          
    
def getPaper_citedConcptes(result):
    """Get an entire dict of works/ id ,concept,cited paper and its concept. 

    Args:
        result (json): content from responses' result

    Returns:
        dict: id,papers_concept,papers_citedconcepts
    """
    
    # return dict content
    id_conceptes_citedconcepts = {}  # final return id ,concepts and cited concepts
    id_paperField = {} # dict of connect with one id and its cited' dict
    paperField = {} # one id with its cited papers' count 
    
    # function begin,cited papers
    cited_by_api_url = ParseWork.getCitedByApiUrl(result)# get  authors' cited paper 
    paperList = parseCitedByApiUrl(cited_by_api_url) # get cited paper list and parse it
    
    for _,paperConcept in paperList.items():
        if paperConcept in paperField:
            paperField[paperConcept] += 1
        else:
            paperField[paperConcept] = 1
            
    # choose Method 1 default，return works' paper concepy
    PaperConceptValue = chooseMethod(result,1)
    
    cited_by_count = ParseWork.getCitedByCount(result)
    
    id_paperField["papers_concept"] = PaperConceptValue
    id_paperField["papers_citedconcepts"] = paperField
    id_paperField["papers_citedcounts"] = cited_by_count
    
    id = ParseWork.getId(result)  # papers' Alex ID
    id_conceptes_citedconcepts[id] = id_paperField
    
    return id_conceptes_citedconcepts


    