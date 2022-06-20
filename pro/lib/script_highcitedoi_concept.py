import time
# import queue
# import threading


from common import getResponse,ParseWork
from parse_url import chooseMethod
from url_tool import splice_url


def getCitedWork(var_doi,cited_work_doi_url,ori_paper_concept):
    """get cited work from multi pages, use cursor - step 2

    Args:
        var_doi (str): doi
        cited_work_doi_url (str): url of cited work
        ori_paper_concept (str): concept of original paper
    """
    start =time.time()
    citedUrl = cited_work_doi_url + "&mailto=1501213957@pku.edu.cn&per-page=50&cursor="
    cur = "*"
    count = 1
    while cur:
        # print(count)
        cited_work_doi_cursor_url = citedUrl + cur
        resultRespone = getResponse(cited_work_doi_cursor_url) # call back cited paper
        if resultRespone:
            data = resultRespone.json()
            cur = data["meta"]["next_cursor"]
            count += 1
            results = data["results"]
            for result in results:
                id = result["id"] # cited papers ids' url
                citedConcepts = chooseMethod(result,1)
                if id and citedConcepts:
                    writeTotxt(var_doi,cited_work_doi_url,ori_paper_concept,id,citedConcepts)       
    end = time.time()
    print('Running time: %s Seconds'%(end-start))
    
    # get_citedDoi_urls = getCitedurl(all_citedpapers_url) # visit url list
    # print(get_citedDoi_urls)
    # doConcurrentCitedUrl(get_citedDoi_urls,cited_work_doi_url)


def writeTotxt(var_doi,cited_work_doi_url,ori_paper_concept,id,citedConcepts):
    """write high cited work in the file - step 3

    Args:
        var_doi (str): doi
        cited_work_doi_url (str): url of cited work
        ori_paper_concept (str): concept of original paper
        id (str): cited papers ids' url
        citedConcepts (str): concept of cited paper
    """
    try:
        with open("docs/high_citedpaper_doi_2.txt","a+",encoding="utf-8") as f:
            f.write(var_doi + "," + cited_work_doi_url + "," + ori_paper_concept + "," + id+ "," + citedConcepts + '\n')
            f.close()
    except Exception as e:
        print("Can not write to file:",e)

def get_high_cited_doi_concept(filePath):
    """main function of get high cited doi's concept - step 1

    Args:
        filePath (str): path of doi

    Returns:
        None: its an executable function
    """
    with open(filePath,"r",encoding="utf-8") as f:
        doi_datas = f.readlines()
        for doi in doi_datas:
            var_doi = doi.rstrip()
            url_str = splice_url(doi)
            if url_str:
                doi_resp = getResponse(url_str) # return requests
                doi_json = doi_resp.json()
                # add ori concepts
                ori_paper_concept = chooseMethod(doi_json,1)
                cited_work_doi_url = ParseWork.getCitedByApiUrl(doi_json)
                if cited_work_doi_url:
                    getCitedWork(var_doi,cited_work_doi_url,ori_paper_concept)
                else:
                    print("can not get cited works' url")
            else:
                continue