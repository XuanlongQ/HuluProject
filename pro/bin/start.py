#!/usr/bin/python
import sys
sys.path.append('/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro')
sys.path.append('/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/lib')
# '/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro' is an example path, please replace it to your relative path

import yaml
# from logging import exception

# local package
# from log import Logger
from lib import script_university_content,script_highcitedoi_concept,script_level0_highcited_concept,script_level0_university_concept
from lib import script_university_type
if __name__ == '__main__':
    # log = Logger('pro/logdata/all.log',level='debug')
    file = open('pro/conf/config.yaml', 'r', encoding="utf-8")
    file_data = file.read()                 
    file.close()
    
    data = yaml.load(file_data,Loader=yaml.FullLoader)    
    print(data)

    # script1 - get universities' content 
    script_university_content.get_university_content(data["Path"]["iped_grid_name_ror"]) # Path - iped_grid_name_ror

    # script2 - get universities' original and destination concepts - level0
    # script_level0_university_concept.get_university_concept_level0(data["Path"]["university_ori_FloderPath"],data["Path"]["university_dst_FloderPath"]) # Path - ori folder of university, dst folder of university level0 
    
    # script3 - merge universities with 4 types  - university_dst_FloderPath ( university_concepts level 0)
    # script_university_type.merge_university_type(data["Path"]["university_dst_FloderPath"])  # output need to update by yourself.
       
    
    ######## for high cited paper #########
    ## script4 - get high cited papers' original and destination concepts - individual script
    ## script_highcitedoi_concept.get_high_cited_doi_concept(data["Path"]["high_cited_doi"]) # Path - high_cited_doi 

    ## script5 - get high cited paper' original and destination concepts - level0 -- individual script
    ## script_level0_highcited_concept.get_high_cited_doi_concept_level0(data["Path"]["high_cited_doi_concept"],data["Path"]["high_cited_doi_concept_level0"]) # Path -ori :high_cited_doi_concept, dst:level0 address