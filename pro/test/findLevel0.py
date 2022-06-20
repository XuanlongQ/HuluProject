conceptTablePath = "concepts.txt"

testDoi = "pro/universities/Albion College.txt"

dstPath = "pro/university_concepts/Albion College.txt"



def findLevel(ori):
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


if __name__ == "__main__":
    with open(testDoi,"r",encoding="utf-8") as f:
        # 10.1126/science.1167742,https://api.openalex.org/works?filter=cites:W2159397589,Sociology,https://openalex.org/W3139425701,Algorithm
        data = f.readlines()
        for _ in data:
            newline = _.rstrip().split(",")
            doi = newline[0]
            cited_by_url = newline[1]
            ori_concept = newline[2]
            dst_url = newline[3]
            dst_concept = newline[4]
            
            
            ori_final_concept = findLevel(ori_concept)
            if ori_final_concept is None:
                ori_final_concept = ori_concept
            
            dst_final_concept = findLevel(dst_concept)
            if dst_final_concept is None:
                dst_final_concept = dst_concept

            
            print(ori_final_concept,dst_final_concept)
            
            try:
                with open(dstPath,"a+",encoding="utf-8") as f:
                    f.write(doi + "," + cited_by_url + "," + ori_final_concept + "," + dst_url + "," + dst_final_concept + "\n")
                    f.close()
            except:
                print("can not match")