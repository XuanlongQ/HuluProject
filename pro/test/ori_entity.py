fosPath = "/Users/xuanlong/Downloads/FieldsOfStudy.nt"


with open(fosPath,"r",encoding="utf-8") as f:
    data = f.readlines()
    ori_list = []
    for _ in data:
        line = _.rstrip().split(" ",2)  
        entity_ID = line[0]
        if entity_ID not in ori_list:
            ori_list.append(entity_ID)
            with open("conceptEntity.txt","a+",encoding="utf-8") as f:
                f.write(entity_ID +"\n")
                f.close()
            
            

        
    