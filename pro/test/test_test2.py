import threading
import time
import queue
 
# 通过多线程来处理Queue里面的任务：
def work(q):
    while True:
        if q.empty():
            return
        else:
            t = q.get()
            print("当前线程sleep {} 秒".format(t))
            time.sleep(1)
 
def main():
    q = queue.Queue()
    for i in range(10):
        q.put(i)  # 往队列里生成消息
    # 单线程
    # work(q)
 
    # 多线程
    thread_num = 20
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=work, args=(q,))
        # args需要输出的是一个元组，如果只有一个参数，后面加，表示元组，否则会报错
        threads.append(t)
 
    for i in range(thread_num):
        threads[i].start()
    for i in range(thread_num):
        threads[i].join()
 
 
if __name__ == "__main__":
    start = time.time()
    main()
    print('耗时：', time.time() - start)
    
    
"""
    
def getCitedurl(all_citedpapers_url):
    newUrls = []
    if all_citedpapers_url:
        for url in all_citedpapers_url:
            baseURL = "https://api.openalex.org/works/"
            paperID = url.split('/')[-1]
            spliceUrl = baseURL + paperID
            newUrls.append(spliceUrl)
        return newUrls
    else:
        return None

def doConcurrentCitedUrl(get_citedDoi_urls,cited_work_doi_url):
    q = queue.Queue()
    for url in get_citedDoi_urls:
        q.put(url.strip())  # 往队列里生成消息
    # 单线程
    # work(q)

    # 多线程
    thread_num = 5
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=parse_citedUrl_work, args=(q,cited_work_doi_url))
        # args需要输出的是一个元组，如果只有一个参数，后面加，表示元组，否则会报错
        threads.append(t)
        
    for i in range(thread_num):
        threads[i].start()
    for i in range(thread_num):
        threads[i].join()

def parse_citedUrl_work(q,cited_work_doi_url):
    while True:
        if q.empty():
            return
        else:
            url = q.get()
            cited_result_single = getResponse(url)
            if cited_result_single:
                dataSingle = cited_result_single.json()
                cited_paper_id = ParseWork.getId(dataSingle)
                cited_paper_concept = chooseMethod(dataSingle,1)     
                
                writeTotxt(cited_work_doi_url,cited_paper_id,cited_paper_concept)
            else:
                cited_paper_id = "NoneType"
                cited_paper_concept = "NoneType"
                writeTotxt(cited_work_doi_url,cited_paper_id,cited_paper_concept) 
"""