import re

fosChildrenPath = "/Users/xuanlong/Downloads/FieldOfStudyChildren.nt"
fosPath = "/Users/xuanlong/Downloads/FieldsOfStudy.nt"


def get_fos(parent_Entity_ID):
    """get parent id 

    Args:
        parent_Entity_ID (str): entity Id you wanna query

    Returns:
        str: entity_ID,level,display name
    """
    # <http://ma-graph.org/entity/185592680> <http://ma-graph.org/property/level> "0"^^<http://www.w3.org/2001/XMLSchema#integer> .
    # <http://ma-graph.org/entity/185592680> <http://xmlns.com/foaf/0.1/name> "Chemistry"^^<http://www.w3.org/2001/XMLSchema#string> .
    with open(fosPath,"r",encoding="utf-8") as f:
        data = f.readlines()
        entity = {}
        for _ in data:
            line = _.rstrip().split(" ",2)  
            entity_ID = line[0]
            specific_value = line[2]
            if parent_Entity_ID == entity_ID: # match this items
                entity["entity_ID"] = parent_Entity_ID
                property_character = line[1].rstrip(">").lstrip("<")
                value = re.search("[^/]+(?!.*/)", property_character, flags=0)
                property_character_value = value.group()   # name ,level
                if property_character_value == "level":
                    level = int(specific_value.split("^^")[0].rstrip('"').lstrip('"')) # type(level) is int
                    entity["level"] = level
                    print(level)
                elif property_character_value == "name":
                    print(specific_value)
                    print("----")
                    name = specific_value.split("^^")[0].rstrip('"').lstrip('"')
                    entity["name"] = name
                    print(name)
                else:
                    continue
            
        if entity:
            a = entity["entity_ID"]
            b = entity["level"]
            c = entity["name"]
            print(a,b,c)
            return a,b,c
                          
        
def get_fos_Children(entityID):
    """get this entity id's parent id

    Args:
        entityID (str): sub entity id

    Returns:
        str: parent entity id
    """
    # <http://ma-graph.org/entity/2777623060> <http://ma-graph.org/property/hasParent> <http://ma-graph.org/entity/12843> .
    with open(fosChildrenPath,"r",encoding="utf-8") as f:
        data = f.readlines()
        for _ in data:
            line = _.rstrip().split(" ")
            child_Entity_ID = line[0]
            parent_Entity_ID = line[2]
            if entityID == child_Entity_ID:
                return parent_Entity_ID
            

def FindRootConcept(entity_ID):
    """give this function a entity id, it will return its  level and displayname 

    Args:
        entity_ID (str): entity id

    Returns:
        str: entity id ,level,display name
    """
    parent_Entity_ID = get_fos_Children(entity_ID) 
    en_ID,level,name = get_fos(parent_Entity_ID)
    return en_ID,level,name
        
if __name__ == "__main__":
    concept_entity_path = "conceptEntity.txt"
    with open(concept_entity_path,"r",encoding="utf-8") as f:
        data = f.readlines()
        for _ in data:
            
            try:
                testID = _.rstrip()
                # testID = "http://ma-graph.org/entity/1576492"
                entity_ID,ori_level,ori_name = get_fos(testID)
                # http://ma-graph.org/entity/1576492,3,Matrix pencil
                level = ori_level
                # level 3
                while level > 0:
                    en_ID,level,name = FindRootConcept(entity_ID)
                    entity_ID = en_ID
                    print(en_ID,level,name)
                    with open("concepts.txt","a+",encoding="utf-8") as f:
                        f.write(testID + "," + str(ori_level) + "," + ori_name + "," 
                                + en_ID + "," + str(level) + "," + name  + "\n")
                        f.close()
            except:
                print("do not have level")
