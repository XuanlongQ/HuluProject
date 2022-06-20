#!/usr/bin/python
import sys
sys.path.append('/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro')
sys.path.append('/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/lib')
# '/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro' is an example path, please replace it to your relative path

import yaml
# from logging import exception

# local package
# from log import Logger
from lib import common,url_tool,parse_url,get_cited_work,get_reference_work
from lib import script_university_content,script_highcitedoi_concept

if __name__ == '__main__':
    # log = Logger('pro/logdata/all.log',level='debug')
    file = open('pro/conf/config.yaml', 'r', encoding="utf-8")
    file_data = file.read()                 
    file.close()
    
    data = yaml.load(file_data,Loader=yaml.FullLoader)    


    # script1 - get universities' content 
    script_university_content.get_university_content(data["Path"]["iped_grid_name_ror"]) # Path - iped_grid_name_ror

    # script2 - get high cited papers' original and destination concepts
    script_highcitedoi_concept.get_high_cited_doi_concept(data["Path"]["high_cited_doi"]) # Path - high_cited_doi 


    """
    #Logger('pro/logdata/error.log', level='error').logger.error('content')
    for url in urls:
        pass
    # mit url
    # url = "https://api.openalex.org/works?mailto=zd675589296@qq.com&per-page=50&filter=publication_year:2020,institutions.ror:https://ror.org/042nb2s44&cursor="
    
    # oxford url
    #url = "https://api.openalex.org/works?mailto=675589296@qq.com&per-page=50&filter=publication_year:2020,institutions.ror:https://ror.org/052gg0110&cursor="
    
    # Munich
    url = "https://api.openalex.org/works?mailto=zd675589295@qq.com&per-page=50&filter=publication_year:2020,institutions.ror:https://ror.org/02kkvpp62&cursor="
    
    # Denmark
    # url = "https://api.openalex.org/works?mailto=zd675589296@qq.com&per-page=50&filter=publication_year:2020,institutions.ror:https://ror.org/04qtj9h94&cursor="
    
    # Add the mailto=you@example.com parameter in your API request, like this: https://api.openalex.org/works?mailto=you@example.com
	# Use polite pool
    # BASE_URL = "https://api.openalex.org"
    # MAIL_ADDRESS = "mailto=zd675589296@qq.com"
    # PER_PAGE = "10"
    # INSTITUTION = "institutions.ror:https://ror.org/042nb2s44"
    # testUrl = BASE_URL + "/works?" + MAIL_ADDRESS + "&per-page=" + PER_PAGE + "&filter=publication_year:2020," + INSTITUTION + "&cursor="
    # print(testUrl)
    

    # 计数页
    count = 0
    cur = "*"
    # writeResq(res)
    while cur:
        start =time.time()
        
        count = count + 1
        print(count)
        ####################################         Work Part         ###################################
        workUrl = url + cur
        print("url is :",workUrl)
        print("cur is:",cur)
        
        resultRespone = common.getResponse(workUrl)
        if resultRespone:
            data = resultRespone.json()
            cur = data["meta"]["next_cursor"]
            resultsWork = data["results"]
            print(cur)
        # else:
        #     continue
            
        # getResultsWork(resultsWork)   
        # get_cited_work.getDisplineWork(resultsWork)
        # if count  < 50 :
        #     pass
        # else:
        get_reference_work.getReferenceWork(resultsWork)
            
        end = time.time()
        print('Running time: %s Seconds'%(end-start))
       
        ####################################         Author Part         ###################################
        # AuthorIdUrl = "https://api.openalex.org/authors/A2903904671" 
        # resultsAuthor = common.getResponseAuthor(AuthorIdUrl)
        # AuthorConcepts = common.getResultsAuthor(resultsAuthor)
        
        ####################################         other Parts         ###################################

        # print(cur,type(cur))
        # writeResq(results) 
"""
        
    

    