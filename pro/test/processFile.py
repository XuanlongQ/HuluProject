
import json

import csv

path ="pro/experimentdata/Denmark.json"


def writetoCsv(papers_concept,papers_citedconcepts):
    file2 = open('csv_file_Denmark.csv', 'a+', encoding='utf-8', newline="")
    csv_write = csv.writer(file2)
    for k,v in papers_citedconcepts.items():
        # print(k,v)
        csv_write.writerow([papers_concept, k, v])
    f.close()
    
    
with open(path, 'r', encoding='utf-8') as f:
    try:
        data = json.load(f)
        for line in data:
            print(line)
            for _,v in line.items():
                if v["papers_citedconcepts"]:
                    papers_concept = v["papers_concept"]
                    papers_citedconcepts = v["papers_citedconcepts"]
                    
                    print(v)
                    
                    writetoCsv(papers_concept,papers_citedconcepts)
                else:
                    print("***")


    except Exception as e:
        print(e)
        f.close()

 




    