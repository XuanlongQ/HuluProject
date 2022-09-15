#!/usr/bin/python
import os
import sys
sys.path.append('/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro')
sys.path.append('/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/lib')
# from logging import exception

# local package
# from log import Logger
from lib import script_university_content,script_highcitedoi_concept,script_level0_highcited_concept,script_level0_university_concept
from lib import script_university_type
from lib import middleware


if __name__ == '__main__':
    
    Yamlcon = middleware.YamlConfig()
    data_yaml = Yamlcon.get_yaml()
    # log = Logger('pro/logdata/all.log',level='debug')
    
    # Function Start

    # ########script1 - get universities' content 
    script_university_content.get_university_content(data_yaml,data_yaml["Path"]["iped_grid_name_ror"]) # Path - iped_grid_name_ror
    
    
    # ########script2 - get universities' original and destination concepts - level0
    # YEAR = data_yaml['URL']['year']
    # university_ori_FloderPath = 'pro'+ os.sep + 'experimentdata' + os.sep + 'universities' + os.sep + YEAR
    # university_dst_FloderPath = 'pro'+ os.sep + 'experimentdata' + os.sep + 'university_concepts' + os.sep + YEAR
    
    # if not os.path.isdir(university_ori_FloderPath):
    #     print("You do run scrip1 first ,no files now")
    #     sys.exit(0)
        
    # if not os.path.isdir(university_dst_FloderPath):    
    #     os.makedirs(university_dst_FloderPath)
    # # Path - ori folder of university, dst folder of university level0 
    # script_level0_university_concept.get_university_concept_level0(university_ori_FloderPath,university_dst_FloderPath) 
    
    
    
    ######## script3 - merge universities with 4 types  - university_dst_FloderPath ( university_concepts level 0)
    # YEAR = data_yaml['URL']['year']
    # universityType_ori_FloderPath = 'pro'+ os.sep + 'experimentdata' + os.sep + 'university_concepts' + os.sep + YEAR
    # universityType_dst_FloderPath = 'pro'+ os.sep + 'experimentdata' + os.sep + 'university_type' + os.sep + YEAR
    
    # if not os.path.isdir(universityType_ori_FloderPath):
    #     print("You do run scrip2 first ,no files now")
    #     sys.exit(0) 
        
    # if not os.path.isdir(universityType_dst_FloderPath):
    #     os.makedirs(universityType_dst_FloderPath)
        
    # script_university_type.merge_university_type(universityType_ori_FloderPath,universityType_dst_FloderPath)  # output need to update by yourself.
       
       
       
       
       
       
       
       
       
       
    ########################## for high cited paper ###################################
    ## script4 - get high cited papers' original and destination concepts - individual script
    ## script_highcitedoi_concept.get_high_cited_doi_concept(data_yaml["Path"]["high_cited_doi"]) # Path - high_cited_doi 

    ## script5 - get high cited paper' original and destination concepts - level0 -- individual script
    ## script_level0_highcited_concept.get_high_cited_doi_concept_level0(data_yaml["Path"]["high_cited_doi_concept"],data_yaml["Path"]["high_cited_doi_concept_level0"]) # Path -ori :high_cited_doi_concept, dst:level0 address