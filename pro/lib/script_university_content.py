import time

import url_tool
import common,get_reference_work


def workFunc(url,university,rorid):
    """import function of get universities' content - step 2

    Args:
        url (str): all universities' iped,doi and their ror
        university (str): displayname
        rorid (str): rorid of this university
    """
    print("now , the university is:",university)
    # count page
    count = 0
    cur = "*"
    while cur:
        start =time.time()
        count = count + 1
        # print(count)
        workUrl = url + cur
        print("url is :",workUrl)
        resultRespone = common.getResponse(workUrl)
        if resultRespone:
            data = resultRespone.json()
            cur = data["meta"]["next_cursor"]
            resultsWork = data["results"]
            print(cur)
        # if count  < 50 :
        #     pass
        # else:
        get_reference_work.getReferenceWork(resultsWork,university,rorid) # do a multiprocessing work
        end = time.time()
        print('Running time: %s Seconds'%(end-start))

def get_university_content(rorPath):
    """import function of get universities' content - step 1

    Args:
        rorPath (str): path of all university 
    """
    with open(rorPath,"r",encoding="utf-8") as f:
        data = f.readlines()
        for _ in data:
            line = _.rstrip().split(",")
            print(line)  # 168546,grid.252000.5,Albion College,https://ror.org/05nnk3913
            rorid = line[3]
            university = line[2]
            if isinstance(rorid,str):
                url = url_tool.clip_url(rorid)
                workFunc(url,university,rorid)
                print("This university has finished:", university)
    