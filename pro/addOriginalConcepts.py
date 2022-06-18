from toolFunc import getResponse,ParseWork
from parseUrl import chooseMethod

filePath = "docs/doi_ori_url.txt"

with open(filePath,"r",encoding="utf-8") as f:
    data = f.readlines()
    for _ in data :
        line = _.rstrip()
        if isinstance(line,str):
            resultRespone = getResponse(line)
            result = resultRespone.json()
            ori_concept =
