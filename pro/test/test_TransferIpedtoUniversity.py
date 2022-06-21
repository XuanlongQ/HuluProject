filePath = "docs/ipeds.txt"
ContentPath = "docs/grids.txt"
rorPath = "docs/ror_grid.txt"

def findGrids(ipeds_id):
    with open(ContentPath,"r",encoding="utf-8") as f:
        data = f.readlines()
        for _ in data:
            line = _.rstrip().split()
            if len(line) > 1:
                ipeds_id_fromgrids = line[0]
                grid_id_fromgrids  = line[1]
                if ipeds_id == ipeds_id_fromgrids:
                    return grid_id_fromgrids
                else:
                    continue

def findROR(grid):
    with open(rorPath,"r",encoding= "utf-8") as f:
        data = f.readlines()
        for _ in data:
            # rorId	name	countryCode	gridId
            line = _.rstrip().split('\t')
            if len(line) > 3:
                rorid = line[0]
                gridid = line[3]
                if grid == gridid:
                    return rorid
                else:
                    continue

with open(filePath,"r",encoding="utf-8") as f:
    data = f.readlines()
    for _ in data:
        line = _.rstrip().split("\t")
        ipeds_id = line[0]
        ipeds_name = line[1]
        print(ipeds_id,ipeds_name)
        
        grid= findGrids(ipeds_id)
        rorid = findROR(grid)
        
        if grid:
            with open("iped_grid.txt","a+",encoding="utf-8") as f:
                f.write(ipeds_id + "," + grid+"," + ipeds_name + "," + rorid + '\n')
                f.close()
                print(ipeds_id,grid,ipeds_name,rorid)
        else:
            continue