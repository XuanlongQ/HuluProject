

import sys



filePath = "docs/doi_university.txt"

if __name__ == '__main__':
    with open(filePath,"r",encoding="utf-8") as f:
        doi_datas = f.readlines()
        for _ in doi_datas:
            line = _.rstrip().split('\t')
            uni = line[0] # str
            doi = line[1] # str
            print("-----")
            first_affilion = uni.split(';')[0]
            print(first_affilion,doi)
            with open("test_doi_university.txt","a+",encoding='utf-8') as f:
                f.write(first_affilion + "," + doi + "\n")
                f.close()

    