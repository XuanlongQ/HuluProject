# local
from common import ParseWork,getResponse
from parse_url import chooseMethod
# from log import Logger

### threading module
import queue
import threading

concurrent = 5

### func part
def getReferenceWork(results,university,rorid):
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
                        if institution["ror"] == rorid:
                            referenced_work_urls = get_reference_urls(result) # referenced urls list
                            if referenced_work_urls:
                                doConcurrent(referenced_work_urls,ori_paper_ID,ori_paper_concept,university) # multi-processing
            #             else:
            #                 continue
            #     else:
            #         continue
            # else:
            #     continue
            
    except Exception as e:
        print("Can not get referenced work:",e)
        # Logger('pro/logdata/error.log', level='error').logger.error(e)

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

def doConcurrent(referenced_work_urls,ori_paper_ID,ori_paper_concept,university):
    """createe a queue and prepare for multi processing

    Args:
        referenced_work_urls (list): reference url 
        ori_paper_ID (str): papers' id
        ori_paper_concept (str): papers' concept
    """
    q = queue.Queue()
    for url in referenced_work_urls:
        q.put(url.strip())  # ????????????????????????
    # ?????????
    # work(q)

    # ?????????
    thread_num = concurrent
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=parse_referenced_work, args=(q,ori_paper_ID,ori_paper_concept,university))
        # args??????????????????????????????????????????????????????????????????????????????????????????????????????
        threads.append(t)

    for i in range(thread_num):
        threads[i].start()
    for i in range(thread_num):
        threads[i].join()
            
def parse_referenced_work(q,ori_paper_ID,ori_paper_concept,university):
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
                writeTotxt(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept,university)
            else:
                referenced_paper_id = "NoneType"
                referenced_paper_concept = "NoneType"
                print(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept)
                writeTotxt(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept,university)
            
def writeTotxt(ori_paper_ID,ori_paper_concept,referenced_paper_id,referenced_paper_concept,university):
    writeToFile = "pro/universities/2011/" + university + ".txt"
    try:
        with open(writeToFile,"a+",encoding="utf-8") as f:
            f.write(ori_paper_ID + "," + ori_paper_concept+ "," + referenced_paper_id +","+ referenced_paper_concept+ '\n')
            f.close()
    except Exception as e:
        print("Can not write to file:",e)
        # Logger('pro/logdata/error.log', level='error').logger.error(e)
                 
    
        