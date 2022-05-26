import requests
import json
import sys

# local
from toolFunc import ParseWork,writeResq
from parseUrl import chooseMethod
from log import Logger

### threading module
import queue
import threading


concurrent = 5
Denmark = "https://ror.org/04qtj9h94"

### func part

def getReferenceWork(results):
    """write referenced content to file

    Args:
        results (_type_): response from url
    """
    try :
        for result in results:
            ori_paper_ID = ParseWork.getId(result)
            if len(ori_paper_ID):
                ori_paper_concept = chooseMethod(result,1)
                
                print(ori_paper_ID,ori_paper_concept)
                
                institutions = ParseWork.getAuthorship(result) # get first author
                if len(institutions):
                    institution = institutions[0]
                    for institution in institutions:
                        if institution["ror"] == Denmark:
                            referenced_work_urls = get_reference_urls(result) # referenced urls list
                            doConcurrent(referenced_work_urls,ori_paper_ID,ori_paper_concept)
                        else:
                            continue
                else:
                    continue
            else:
                continue
            
    except Exception as e:
        print("Can not get referenced work:",e)
        Logger('pro/logdata/error.log', level='error').logger.error(e)

def get_reference_urls(result):
    urls = []
    referenced_works = ParseWork.getReferencedWorks(result)
    for referenced_work in referenced_works:
        baseURL = "https://api.openalex.org/works/"
        paperID = referenced_work.split('/')[-1]
        spliceUrl = baseURL + paperID
        urls.append(spliceUrl)
    # print(urls)
    return urls

def doConcurrent(referenced_work_urls,ori_paper_ID,ori_paper_concept):
    q = queue.Queue()
    for url in referenced_work_urls:
        q.put(url.strip())  # 往队列里生成消息
    # 单线程
    # work(q)

    # 多线程
    thread_num = concurrent
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=parse_referenced_work, args=(q,ori_paper_ID,ori_paper_concept))
        # args需要输出的是一个元组，如果只有一个参数，后面加，表示元组，否则会报错
        threads.append(t)

    for i in range(thread_num):
        threads[i].start()
    for i in range(thread_num):
        threads[i].join()
            
def parse_referenced_work(q,ori_paper_ID,ori_paper_concept):
    
    while True:
        if q.empty():
            return
        else:
            url = q.get()
            reference_result_single = getReferenceResult(url)
            referenced_paper_id = ParseWork.getId(reference_result_single)
            referenced_paper_concept = chooseMethod(reference_result_single,1)
            
            try:
                with open("pro/experimentdata/testDenmark.txt","a+",encoding="utf-8") as f:
                    f.write(ori_paper_ID + "," + ori_paper_concept + "," + referenced_paper_id +","+ referenced_paper_concept + '\n')
                    f.close()
            except Exception as e:
                print("Can not get referenced paper:",e)
                Logger('pro/logdata/error.log', level='error').logger.error(e)
                

def getReferenceResult(ourl):
    try:
        resp = requests.get(ourl).json()
        return resp
    except Exception as e:
        print("Can not get correct response:",e)
        Logger('pro/logdata/error.log', level='error').logger.error(e)
    
#################### threading  end #####################   


# def get_Referenced_paper(result):
#     """get referenced content and could write to json

#     Args:
#         result (json): response from original url

#     Returns:
#         dict: original paper - referenced paper
#     """
#     try:
#         id_origianl_paper = ParseWork.getId(result) # ori
#         paper_concept = chooseMethod(result,1)
        
#         referenced_works = ParseWork.getReferencedWorks(result) #list[str]
        
#         # return dict content
#         id_conceptes_reference_concepts = {}  # final return id ,concepts and cited concepts
#         id_paperField = {}
#         reference_count = {} # dict of connect with one id and its cited' dict

#         for referenced_work in referenced_works:
#             # "https://openalex.org/W1985185445"
            
#             resultWork = parse_Referenced_paper(referenced_work)
#             Paper_referenced_Value = chooseMethod(resultWork,1)
#             print("now is parsing :",referenced_work,Paper_referenced_Value)

#             if Paper_referenced_Value in reference_count:
#                 reference_count[Paper_referenced_Value] += 1
#             else:
#                 reference_count[Paper_referenced_Value] = 1
            

#         id_paperField["papers_concept"] = paper_concept
#         id_paperField["papers_reference_concepts"] = reference_count
#         id_conceptes_reference_concepts[id_origianl_paper] = id_paperField
        
#         return id_conceptes_reference_concepts
#     except Exception as e:
#         print("Can not get referenced paper:",e)
#         Logger('pro/logdata/error.log', level='error').logger.error(e)
    
# def getReferenceWork(results):
#     """write referenced content to file

#     Args:
#         results (_type_): response from url
#     """
#     try:
#         for result in results:
#             global Denmark
#             institutions = ParseWork.getAuthorship(result) # get first author
#             if len(institutions):
#                 institution = institutions[0]
#                 for institution in institutions:
#                     if institution["ror"] == Denmark:
#                         ReferencedWork = get_Referenced_paper(result)
#                         writeResq(ReferencedWork)
#                     else:
#                         continue
#             else:
#                 continue
#     except Exception as e:
#         print("Can not get referenced work:",e)
#         Logger('pro/logdata/error.log', level='error').logger.error(e)
        
# def parse_Referenced_paper(referenced_work):
#     """return a response of referenced work

#     Args:
#         referenced_work (str): url

#     Returns:
#         response: response of referenced work
#     """
#     baseURL = "https://api.openalex.org/works/"
#     paperID = referenced_work.split('/')[-1]
    
#     spliceUrl = baseURL + paperID # "https://api.openalex.org/works/W3095157763"
    
#     try:
#         resp = requests.get(spliceUrl).json()
#         return resp
#     except Exception as e:
#         print("Can not get correct response:",e)
#         Logger('pro/logdata/error.log', level='error').logger.error(e)
        