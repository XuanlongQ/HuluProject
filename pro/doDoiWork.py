import time
# import queue
# import threading


from toolFunc import getResponse,ParseWork
from parseUrl import chooseMethod

filePath = "docs/doi.txt"

def spliceStr(_):
    if isinstance(_,str):
        prefix = "https://api.openalex.org/works/https://doi.org/"
        url_str = prefix + _.rstrip()
        return url_str
    else:
        return None

def getCitedWork(cited_work_doi_url):
    start =time.time()
    citedUrl = cited_work_doi_url + "&mailto=675589296@pku.edu.cn&per-page=50&cursor="
    cur = "*"
    count = 1
    while cur:
        print(count)
        cited_work_doi_cursor_url = citedUrl + cur
        resultRespone = getResponse(cited_work_doi_cursor_url)
        if resultRespone:
            data = resultRespone.json()
            cur = data["meta"]["next_cursor"]
            count += 1
            results = data["results"]
            for result in results:
                id = result["id"] # cited papers ids' url
                citedConcepts = chooseMethod(result,1)
                if id and citedConcepts:
                    writeTotxt(cited_work_doi_url,id,citedConcepts)       
    end = time.time()
    print('Running time: %s Seconds'%(end-start))
    
    # get_citedDoi_urls = getCitedurl(all_citedpapers_url) # visit url list
    # print(get_citedDoi_urls)
    # doConcurrentCitedUrl(get_citedDoi_urls,cited_work_doi_url)


def writeTotxt(cited_work_doi_url,id,citedConcepts):
    try:
        with open("pro/experimentdata/testDoi0610-1.txt","a+",encoding="utf-8") as f:
            f.write(cited_work_doi_url + "," + id+ "," + citedConcepts + '\n')
            f.close()
    except Exception as e:
        print("Can not write to file:",e)

if __name__ == '__main__':
    with open(filePath,"r",encoding="utf-8") as f:
        doi_datas = f.readlines()
        for _ in doi_datas:
            url_str = spliceStr(_)
            if url_str:
                doi_resp = getResponse(url_str) # return requests
                doi_json = doi_resp.json()
                cited_work_doi_url = ParseWork.getCitedByApiUrl(doi_json)
                if cited_work_doi_url:
                    getCitedWork(cited_work_doi_url)
                else:
                    print("can not get cited works' url")
            else:
                continue