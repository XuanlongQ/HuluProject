#!/usr/bin/python
import time
import json
import random
import requests
from middleware import PROXY,USER_AGENTS
#from logging import exception

# local package
#from log import Logger

"""
Get information through openAlex ID
Mainly focus on five basic entities
"""
#log = Logger('pro/logdata/all.log',level='debug')


class ParseWork:
    """ parse all the items from work entity
    """
    
    @staticmethod
    def getReferencedWorks(result):
        referencedWorks = result["referenced_works"]
        return referencedWorks
    
    @staticmethod
    def getAbstract(result):
        """_summary_

        Args:
            results (json): response from url

        Returns:
            str: abstract str
        """
        abstract_inverted_index = result["abstract_inverted_index"]
        str = " "
        seq = [ _ for _ in abstract_inverted_index.keys() ] # abstract list
        abstract = str.join(seq) # abstract str
        # print(abstract,type(abstract))
        try:
            #log.logger.info("return abstract.")
            return abstract # abstract str
        except Exception as e:
            print("Return abstract error:",e)
            #Logger('pro/logdata/error.log', level='error').logger.error(e) 
    
    @staticmethod
    def getCitedByCount(result):
        """Get works' cited counts

        Args:
            result (json): response from url

        Returns:
            int: cited_by_count
        """
        cited_by_count = result["cited_by_count"]
        return cited_by_count
  
    @staticmethod
    def getId(result):
        """get unique id in openAlex

        Args:
            result (json): response from url

        Returns:
            str: unique id
        """
        try:
            id = result["id"]  # unique paper ID, str
            if id:
                return id
            else:
                return None
        except Exception as e:
            print("Can not get paper id error:",e)
            #Logger('pro/logdata/error.log', level='error').logger.error(e) 

            
    
    @staticmethod
    def getPublicationYear(result):
        """get publication year

        Args:
            result (json): response from url

        Returns:
            int: year of publicate
        """
        publication_year = result["publication_year"] # year of pub,int
        return publication_year
    
    @staticmethod
    def getFirstAuthor_Institution_Countrycode(result):
        """get first authors' name,institution,countrycode

        Args:
            result (json): response from url

        Returns:
            dict,str,str: the results of first authors' dict,institution,countrycode
        """
        authorships = result["authorships"] # all the authors' information,list
        first_author = [x for x in authorships][0] # authors - first author,dict - add test cases, and need be confirmed
        institutions_author = first_author["raw_affiliation_string"] # institutions of first author,str
        countrycode_author = first_author["institutions"][0]["country_code"] # country code of first author,str
        return first_author,institutions_author,countrycode_author
    
    @staticmethod
    def getCitedByApiUrl(result):
        """Get cited paper from works

        Args:
            result (json): response from url

        Returns:
            str: cited_by_api_url
        """
        cited_by_api_url = result["cited_by_api_url"] # references cited in the data
        if isinstance(cited_by_api_url,str):
            return cited_by_api_url
        else:
            return None
      
    @staticmethod
    def getAuthorship(result):
        """Use to pop first author instutition informations

        Args:
            result (json): content from responses' result

        Returns:
            list: institutions
        """
        authorships = result["authorships"]
        for authorship in authorships:
            # print("authorship si type:",type(authorship))
            try:
                if authorship["author_position"] == "first":
                    institutions = authorship["institutions"]
                    # print(type(institutions))
                    if institutions:
                        return institutions
                    else:
                        return None
                else:
                    #log.logger.info("this is authors from non-first author.")
                    continue
            except Exception as e:
                print("Return pop first author error:",e)
                #Logger('pro/logdata/error.log', level='error').logger.error(e) 
    
    """Two methods to find concept

    Returns:
        _type_: the result of the method you use
    """
    
    @staticmethod
    def findTopLevel(result):
        """find the top level subject , level 0

        Args:
            concepts (json): content from responses' result

        Returns:
            str: top level subject
        """
        try:
            concepts = result["concepts"]
            conceptDict = {}
            for concept in concepts:
                subject = concept["display_name"]
                level = concept["level"]
                conceptDict[subject] = int(level)
            conceptList = sorted(conceptDict.items(), key = lambda kv:(kv[1], kv[0]),reverse=False) # sorted conceptlist,list
            # print(conceptList,type(conceptList))  
            topLevel = conceptList[0][0]
            #log.logger.info("return top level concept.")
            return topLevel # top level, str
        except Exception as e:
            print("Return top Content error:",e)
            #Logger('pro/logdata/error.log', level='error').logger.error(e) 
    
    @staticmethod
    def findHighestScoreConcept(result):
        """_summary_

        Args:
            concepts (json): content from responses' result

        Returns:
            str: highest score subject
        """
        try:
            concepts = result["concepts"]
            conceptDict = {}
            for concept in concepts:
                subject = concept["display_name"]
                score = concept["score"]
                conceptDict[subject] = float(score)
                #print(concept,type(concept))
            conceptList = sorted(conceptDict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) # sorted conceptlist,list
            # print(conceptList,type(conceptList))    
            HighestScoreConcept = conceptList[0][0]
            #log.logger.info("return highest score concept.")
            return HighestScoreConcept # Highest Score, str
        
        except Exception as e:
            print("Return top Content error:",e)
            #Logger('pro/logdata/error.log', level='error').logger.error(e)                      
class ParseAuthor:
    """Parse the content of Author Id
    """
    
    @staticmethod
    def getResultsAuthor(result):
        """Parse list of x_concepts

        Args:
            result (dict): dict of one x_concept

        Returns:
            str, str: authorId ,authorConcept
        """
        authorId = result["id"]
        authorConcept = result["display_name"]
        # print(authorId,type(authorId))
        # print(authorConcept,type(authorConcept))
        return authorId,authorConcept # str,str
    
class ParseVenue:
    pass

class ParseInstitution:
    pass

class ParseConcept:
    pass
   
   
# result to files
def writeResq(res):
    """write json to file 

    Args:
        res (None): no return value
    """
    try:
        with open("pro/experimentdata/referencedDenmarkTest.json","a+",encoding= "utf-8") as f:
            json.dump(res, f, indent=4)
            f.write(",")
            f.close()
                
    except Exception as e:
        print("write error:",e)
        #Logger('pro/logdata/error.log', level='error').logger.error(e)


'''
proxy = '127.0.0.1:9180' //这里写代理的ip及端口
proxies = {
     'http': 'http://' + proxy,
     'https': 'https://' + proxy
 }
...
result = s.get(url=req, params=param, headers=headers, verify=False, proxies=proxies)

'''
      
NETWORK_STATUS = True # 判断状态变量

headers = {'Connection': 'close',
           'User-Agent': random.choice(USER_AGENTS)
           }

proxies = {
     'http': 'http://' + random.choice(PROXY)    
}

def getResponse(url):
    try:
        resp = requests.get(url,timeout=10,verify=False,headers=headers,proxies=proxies)
        if resp.status_code == 200:
            return resp
        else:
            print(resp.status_code)
            return None
    except requests.exceptions.Timeout:
        global NETWORK_STATUS
        NETWORK_STATUS = False
        if NETWORK_STATUS == False:
            #timeout
            for i in range(1,10):
                print("request timeout, the %s repeat!",i)
                resp = requests.get(url,timeout=10,verify=False,headers=headers,proxies=proxies)
                time.sleep(5)
                if resp.status_code == 200:
                    return resp
                else:
                    #Logger('pro/logdata/error.log', level='error').logger.error("can not get response")
                    return None
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        resp = requests.get(url,timeout=10,verify=False,headers=headers,proxies=proxies)
        if resp.status_code == 200:
            return resp
        else:
            #Logger('pro/logdata/error.log', level='error').logger.error("connect error")
            return None
    
    
        
