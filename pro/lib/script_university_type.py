import os

def match_university_type(university):
    filePath = "docs/school_type.txt"
    with open(filePath,"r",encoding="utf-8") as f:
        data = f.readlines()
        for _ in data:
            newline = _.rstrip().split("\t")
            university_name = newline[2]
            university_status = newline[3]
            university_disipline = newline[4]
            # print(university_name,university_status,university_disipline)
            if university == university_name:
                return university_status,university_disipline
            else:
                continue
            
def write_to_file(university,filePath,dstPath):
    with open(filePath,"r",encoding="utf-8") as f:
        data = f.readlines()
        for _ in data:
            print(_)
            with open(dstPath,"a+",encoding="utf-8") as f_output:
                f_output.write(university+ "," +_)
                f_output.close()
                
def merge_university_type(university_FloderPath):
    # university_FloderPath = "pro/experimentdata/university_concepts/2021"
    fileName = os.listdir(university_FloderPath)
    fileName.sort()
    for file in fileName:
        filePath = university_FloderPath + "/" + file
        university = file.split(".")[0]
        university_status,university_disipline = match_university_type(university)
        #print(university,university_status,university_disipline)
        print(filePath)
        if university_status == "0" and university_disipline == "0":
            dstPath = "pro/experimentdata/university_type/2011/low_status_science.txt"
        elif university_status == "0" and university_disipline == "1":
            dstPath = "pro/experimentdata/university_type/2011/low_status_liberal_arts.txt"
        elif university_status == "1" and university_disipline == "1":
            dstPath = "pro/experimentdata/university_type/2011/high_status_liberal_arts.txt"
        elif university_status == "1" and university_disipline == "0":
            dstPath = "pro/experimentdata/university_type/2011/high_status_science.txt"
        else:
            dstPath = None
        print(university,dstPath)
        write_to_file(university,filePath,dstPath)
        
        
    