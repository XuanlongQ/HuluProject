
import json

import csv

path ="pro/experimentdata/referencedDenmarkTest.json"


def writetoCsv(papers_concept,papers_reference_concepts):
    file2 = open('csv_file_referencedDenmarkTest.csv', 'a+', encoding='utf-8', newline="")
    csv_write = csv.writer(file2)
    for k,v in papers_reference_concepts.items():
        # print(k,v)
        csv_write.writerow([papers_concept, k, v])
    f.close()
    
    
with open(path, 'r', encoding='utf-8') as f:
    try:
        data = json.load(f)
        for line in data:
            print(line)
            for _,v in line.items():
                if v["papers_reference_concepts"]:
                    papers_concept = v["papers_concept"]
                    papers_reference_concepts = v["papers_reference_concepts"]
                    
                    print(v)
                    
                    writetoCsv(papers_concept,papers_reference_concepts)
                else:
                    print("***")


    except Exception as e:
        print(e)
        f.close()

 




    