import os

universityFloderPath = "pro/universities"
university_dst_FloderPath = "pro/university_concepts"
conceptTablePath = "concepts.txt"


def findLevel(ori):
    """find concept level

    Args:
        ori (str): concept of you want query

    Returns:
        str: level 0 concept
    """
    with open(conceptTablePath,"r",encoding="utf-8") as f:
        data = f.readlines()
        for _ in data:
            # <http://ma-graph.org/entity/2989365779>,3,Neural network modeling,<http://ma-graph.org/entity/11413529>,1,Algorithm
            newline = _.rstrip().split(",")
            sub_concept = newline[2]
            par_concept = newline[5]
            par_concept_level = newline[4]
            #print(newline)
            #<http://ma-graph.org/entity/73782692>,2,Random error,<http://ma-graph.org/entity/11413529>,1,Algorithm
            #<http://ma-graph.org/entity/73782692>,2,Random error,<http://ma-graph.org/entity/33923547>,0,Mathematics
            if ori == sub_concept:
                # again judege
                if par_concept_level == "0":
                    return par_concept
                else:
                    continue
            elif ori == par_concept:
                if par_concept_level == "0":
                    return par_concept
                else:
                    return findLevel(sub_concept)
            else:
                continue

def workFun(filePath,file):
    """use to processing multi-path

    Args:
        filePath (str): universitys' filepath
        file (str): the address you want to writr your file
    """
    with open(filePath,"r",encoding="utf-8") as f:
        # 10.1126/science.1167742,https://api.openalex.org/works?filter=cites:W2159397589,Sociology,https://openalex.org/W3139425701,Algorithm
        # https://openalex.org/W3209883632,Political science,https://openalex.org/W2161643046,Demography
        data = f.readlines()
        for _ in data:
            newline = _.rstrip().split(",")
            ori_url = newline[0]
            ori_concept = newline[1]
            dst_url = newline[2]
            dst_concept = newline[3]
            
            ori_final_concept = findLevel(ori_concept)
            # if ori_final_concept is None:
            #     ori_final_concept = ori_concept
            
            dst_final_concept = findLevel(dst_concept)
            # if dst_final_concept is None:
            #     dst_final_concept = dst_concept

            
            print(ori_final_concept,dst_final_concept)
            
            try:
                with open(file,"a+",encoding="utf-8") as f:
                    f.write(ori_url  + "," + ori_final_concept + "," + dst_url + "," + dst_final_concept + "\n")
                    f.close()
            except:
                print("can not match")


if __name__ == "__main__":
    fileName = os.listdir(universityFloderPath)
    fileName.sort()
    for file in fileName:
        filePath = universityFloderPath + "/" + file
        dstFilename = university_dst_FloderPath + "/" + file
        workFun(filePath,dstFilename)
        #print(filePath,dstFilename)
        print(file ,"has done")
    print("work is finished")
    