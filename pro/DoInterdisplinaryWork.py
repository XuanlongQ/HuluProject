#!/usr/bin/python

from toolFunc import ParseWork
from parseUrl import chooseMethod




def getDisplineWork(results):
    for result in results:
        paperField = {}
        id = ParseWork.getId(result)  # papers' Alex ID
        print(result)
        institutions = ParseWork.getAuthorship(result)
        
        chosenConcept = chooseMethod(1)
        conceptValue = chosenConcept(result)
        
        # if conceptValue in paperField: #直接判断key在不在字典中
        #     paperField[conceptValue]+=1
        # else:
        #     paperField[conceptValue]=1
        
        
        print(id,institutions)
        print(  "*****"  )
        print(conceptValue)
        break
    