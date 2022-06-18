#!/usr/bin/python

import time
import json
import random
import requests

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

      
NETWORK_STATUS = True # 判断状态变量


'''
proxy = '127.0.0.1:9180' //这里写代理的ip及端口
proxies = {
     'http': 'http://' + proxy,
     'https': 'https://' + proxy
 }
...
result = s.get(url=req, params=param, headers=headers, verify=False, proxies=proxies)

'''



USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)"
    
   ]

# https://free.kuaidaili.com/free/inha/
proxy = [
            '202.55.5.209:8090',"183.247.199.114:30001","183.247.211.50:30001","122.9.101.6:8888",
            "47.106.105.236:80","122.9.101.6:8888","47.106.105.236:80","183.247.211.50:30001",
            "111.3.118.247:30001"   
        ]
headers = {'Connection': 'close',
           'User-Agent': random.choice(USER_AGENTS)
           }

proxies = {
     'http': 'http://' + random.choice(proxy)    
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
    
    
        
