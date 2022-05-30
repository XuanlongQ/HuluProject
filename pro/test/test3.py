# import json

# path ="pro/experimentdata/testDenmark2.txt"


# # https://openalex.org/W3095157763,Computer science,https://openalex.org/W2073372703,Environmental science
# # https://openalex.org/W3095157763,Computer science,https://openalex.org/W2567881914,Business
# # https://openalex.org/W3095157763,Computer science,https://openalex.org/W3023217740,Business

# with open(path, 'r', encoding='utf-8') as f:
#     papers_referenced_concepts = {}
    
#     for line in f.readlines():
#         newline = line.split(",")
#         paper_id = newline[0]
#         paper_concept = newline[1]
#         paper_reference = newline[2]
#         paper_reference_concept = newline[3]
        
#         paper_concepts_dict = {}
        
#         if paper_concept in paper_concepts_dict.keys():
#             v = paper_concepts_dict.values()
#             if paper_reference_concept in paper_concepts_dict.keys():
#                 v[paper_reference_concept] += 1
#             else:
#                 v[paper_reference_concept] = 1

#         else:
#             paper_concepts_dict["paper_concept"] = paper_concept
            
#         print(paper_concepts_dict)


# import random

# for i in range(10):
#     a = random.randint(1,10000)
#     print(a)
    