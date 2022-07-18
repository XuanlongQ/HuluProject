# HuluProject
get data from openAlex and do some data analysis

## _1、Steps_:
### Method1:
#### Get the program
```
git clone https://github.com/XuanlongQ/HuluProject.git
```
#### Update requirements.txt dependence go get the python requirements
```
pip install -r requirements.txt
```
#### Run main file
```
cd HuluProject/
python3 pro/bin/start.py
```

### Method2 
```
sh start_py.sh
```

# _2、Other_
## 2.1 key files illustraction
docs: all the universities' attributes
- docs/doi_ori_url.txt: doi url of OpenAlex (support)
- docs/doi.txt: universities' doi (support)
- docs/doi_university.txt: universities' doi and their name (support)
- docs/grids.txt:universities' iped,grid (support)
- docs/high_citedpaper_doi.txt: high cited papers' doi and openAlex url (support)
- **docs/iped_grid_ror_backup.txt: universities' iped,grid,openalAlex ror (key file)**
- docs/iped_grid.txt: universities' iped,grid (support)
- docs/ipeds.txt: universities' iped (support)
- docs/ror_grid.txt:universities' ror,grid (support)
- docs/school_type.txt: universities' type (support)


**concepts.txt: all concepts level ()**
conceptEntity.txt: parse concept - do not delete this file

pro: all the program code
- pro/bin: 
    - pro/bin/start.py : please confirm which script you want to apply
    - pro/bin/r_clustring.R : r clustering algorithm
- pro/conf: config.yaml file for path config
- pro/lib: all code 


pro/experimentdata : all the experiment data
- pro/experimentdata/r_image: r image
- pro/experimentdata/r_image_csv: csv data of r image
- pro/experimentdata/universities: original data of craweled data - sublevel
- pro/experimentdata/university_concepts: original data of craweled data - level 0
- pro/experimentdata/university_type: merged data

## 2.2 Descripton of scripts
### 1、script1 - script_university_content
Using for crawl data from path (data["Path"]["iped_grid_name_ror"])

### 2、script2 - script_level0_university_concept
Using for transfer universities' concept from sublevel to level 0, it must run after script1

### 3、script3 - script_university_type
Using for transfer script2's result to 4 types

### 4、script4 & script5 
4.1 get high cited papers' original and destination concepts
4.2 get high cited paper' original and destination concepts - level0