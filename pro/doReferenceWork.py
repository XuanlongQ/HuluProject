import requests
import json
import sys

# local
from toolFunc import ParseWork,getResponse
from parseUrl import chooseMethod
from log import Logger

### threading module
import queue
import threading


concurrent = 5
Denmark = "https://ror.org/04qtj9h94"
Mit = "https://ror.org/042nb2s44"
Oxford = "https://ror.org/052gg0110"
Munich = "https://ror.org/02kkvpp62"

### func part

def getReferenceWork(results):
    """write referenced content to file

    Args:
        results (_type_): response from url
    """
    try :
        for result in results:
            ori_paper_ID = ParseWork.getId(result)
            if ori_paper_ID:
                ori_paper_concept = chooseMethod(result,1)
                #print(ori_paper_ID,ori_paper_concept)
                institutions = ParseWork.getAuthorship(result) # get first author
                if institutions:
                    institution = institutions[0]
                    for institution in institutions:
                        if institution["ror"] == Mit:
                            referenced_work_urls = get_reference_urls(result) # referenced urls list
                            doConcurrent(referenced_work_urls,ori_paper_ID,ori_paper_concept)
            #             else:
            #                 continue
            #     else:
            #         continue
            # else:
            #     continue
            
    except Exception as e:
        print("Can not get referenced work:",e)
        Logger('pro/logdata/error.log', level='error').logger.error(e)

def get_reference_urls(result):
    """get a list of reference

    Args:
        result (json): response from url

    Returns:
        list: reference lists
    """
    urls = []
    referenced_works = ParseWork.getReferencedWorks(result)
    if referenced_works:
        for referenced_work in referenced_works:
            baseURL = "https://api.openalex.org/works/"
            paperID = referenced_work.split('/')[-1]
            spliceUrl = baseURL + paperID
            urls.append(spliceUrl)
        return urls
    else:
        return None

def doConcurrent(referenced_work_urls,ori_paper_ID,ori_paper_concept):
    """createe a queue and prepare for multi processing

    Args:
        referenced_work_urls (list): reference url 
        ori_paper_ID (str): papers' id
        ori_paper_concept (str): papers' concept
    """
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
    """start processing

    Args:
        q (queue): queue of reference list
        ori_paper_ID (str): papers' id
        ori_paper_concept (str): papers' concept
    """
    while True:
        if q.empty():
            return
        else:
            url = q.get()
            reference_result_single = getResponse(url)
            if reference_result_single:
                dataSingle = reference_result_single.json()
                referenced_paper_id = ParseWork.getId(dataSingle)
                referenced_paper_concept = chooseMethod(dataSingle,1)     
                print(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept)
                writeTotxt(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept)
            else:
                referenced_paper_id = "NoneType"
                referenced_paper_concept = "NoneType"
                print(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept)
                writeTotxt(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept)
            


def writeTotxt(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept):
    try:
        with open("pro/experimentdata/testMit0531-1.txt","a+",encoding="utf-8") as f:
            f.write(ori_paper_ID + "," + ori_paper_concept+ "," + referenced_paper_id +","+ referenced_paper_concept+ '\n')
            f.close()
    except Exception as e:
        print("Can not write to file:",e)
        Logger('pro/logdata/error.log', level='error').logger.error(e)
                 

def getReferenceResult(ourl):
    try:
        resp = requests.get(ourl).json()
        return resp
    except Exception as e:
        print("Can not get correct response:",e)
        Logger('pro/logdata/error.log', level='error').logger.error(e)
    
        