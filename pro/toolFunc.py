#!/usr/bin/python

from logging import exception

# local package
from log import Logger 

"""
Get information through openAlex ID
Mainly focus on five basic entities
"""
log = Logger('pro/logdata/all.log',level='debug')


class ParseWork:
    """ parse all the items from work entity
    """
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
            log.logger.info("return abstract.")
            return abstract # abstract str
        except Exception as e:
            print("Return abstract error:",e)
            Logger('pro/logdata/error.log', level='error').logger.error(e) 
                      
    @staticmethod
    def getId(result):
        """get unique id in openAlex

        Args:
            result (json): response from url

        Returns:
            str: unique id
        """
        id = result["id"]  # unique paper ID, str
        return id
    
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
        """get cited papers' url

        Args:
            result (json): response from url

        Returns:
            str: the url of cited papers
        """
        cited_by_api_url = result["cited_by_api_url"] # references cited in the data
        return cited_by_api_url
        
                    
                
class ParseAuthor:
    pass

class ParseVenue:
    pass

class ParseInstitution:
    pass

class ParseConcept:
    pass


class FindConcept:
    """Two methods to find concept

    Returns:
        _type_: the result of the method you use
    """
    
    @staticmethod
    def findTopLevel(concepts):
        """find the top level subject , level 0

        Args:
            concepts (json): content from responses' result

        Returns:
            str: top level subject
        """
        conceptDict = {}
        for concept in concepts:
            subject = concept["display_name"]
            level = concept["level"]
            conceptDict[subject] = int(level)
        conceptList = sorted(conceptDict.items(), key = lambda kv:(kv[1], kv[0]),reverse=False) # sorted conceptlist,list
        print(conceptList,type(conceptList))
        
        try:
            topLevel = conceptList[0][0]
            log.logger.info("return top level concept.")
            return topLevel # top level, str
        except Exception as e:
            print("Return top Content error:",e)
            Logger('pro/logdata/error.log', level='error').logger.error(e) 
    
    @staticmethod
    def findHighestScoreConcept(concepts):
        """_summary_

        Args:
            concepts (json): content from responses' result

        Returns:
            str: highest score subject
        """
        conceptDict = {}
        for concept in concepts:
            subject = concept["display_name"]
            score = concept["score"]
            conceptDict[subject] = float(score)
            #print(concept,type(concept))
        conceptList = sorted(conceptDict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) # sorted conceptlist,list
        print(conceptList,type(conceptList))    
        
        try:
            HighestScoreConcept = conceptList[0][0]
            log.logger.info("return highest score concept.")
            return HighestScoreConcept # Highest Score, str
        except Exception as e:
            print("Return top Content error:",e)
            Logger('pro/logdata/error.log', level='error').logger.error(e) 
            