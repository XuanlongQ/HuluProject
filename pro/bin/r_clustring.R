# all the path need to be updated

library(igraph)
library(ggrepel)
library(ggraph)
library(tidygraph)
library(tidyverse)

path1_high_status_liberal_arts = "/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/university_type/2011/high_status_liberal_arts.txt" # 18534
path1_high_status_science = "/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/university_type/2011/high_status_science.txt" # 2221276
path1_low_status_liberal_arts = "/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/university_type/2011/low_status_liberal_arts.txt"#16275
path1_low_status_science = "/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/university_type/2011/low_status_science.txt" # 1188090

# read data from text to data frame
df_hsla <- read.delim(path1_high_status_liberal_arts, header = FALSE, sep = ",", dec = ".")
df_hss <- read.delim(path1_high_status_science, header = FALSE, sep = ",", dec = ".")
df_lsla <- read.delim(path1_low_status_liberal_arts, header = FALSE, sep = ",", dec = ".")
df_lss <- read.delim(path1_low_status_science, header = FALSE, sep = ",", dec = ".")

# rename cols origin and destination
names(df_hsla)[names(df_hsla) == 'V3'] <- "origin"
names(df_hsla)[names(df_hsla) == 'V5'] <- "destination"

names(df_hss)[names(df_hss) == 'V3'] <- "origin"
names(df_hss)[names(df_hss) == 'V5'] <- "destination"

names(df_lsla)[names(df_lsla) == 'V3'] <- "origin"
names(df_lsla)[names(df_lsla) == 'V5'] <- "destination"

names(df_lss)[names(df_lss) == 'V3'] <- "origin"
names(df_lss)[names(df_lss) == 'V5'] <- "destination"

## get v2 v4 to data frame
drops <- c("V1","V2","V4")
df_hsla <- df_hsla[ , !(names(df_hsla) %in% drops)]
df_hss <- df_hss[ , !(names(df_hss) %in% drops)]
df_lsla <- df_lsla[ , !(names(df_lsla) %in% drops)]
df_lss <- df_lss[ , !(names(df_lss) %in% drops)]

## output csv file
outPath_hsla  = "/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/r_image_csv/2011/df_hsla_2011.csv"
outPath_hss = "/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/r_image_csv/2011/df_hss_2011.csv"
outPath_lsla = "/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/r_image_csv/2011/df_lsla_2011.csv"
outPath_lss = "/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/r_image_csv/2011/df_lss_2011.csv"


write.csv(df_hsla,outPath_hsla, row.names = FALSE)
write.csv(df_hss,outPath_hss, row.names = FALSE)
write.csv(df_lsla,outPath_lsla, row.names = FALSE)
write.csv(df_lss,outPath_lss, row.names = FALSE)


## clustering and sample method

df_hsla <- read.csv(outPath_hsla, header = TRUE)
df_hss <- read.csv(outPath_hss, header = TRUE)
df_lsla <- read.csv(outPath_lsla, header = TRUE)
df_lss <- read.csv(outPath_lss, header = TRUE)

library('dplyr')

set.seed(123)

# sample rows
df_hsla <- sample_n(df_hsla, 14336)  
df_hss <- sample_n(df_hss, 14336)  
df_lsla <- sample_n(df_lsla, 14336)  
df_lss <- sample_n(df_lss, 14336)  

# cluster
g_hsla <- graph.data.frame(df_hsla, directed = TRUE)
g_hss <- graph.data.frame(df_hss, directed = TRUE)
g_lsla <- graph.data.frame(df_lsla, directed = TRUE)
g_lss <- graph.data.frame(df_lss, directed = TRUE)

oc_hsla <- cluster_optimal(g_hsla)
oc_hss <- cluster_optimal(g_hss)
oc_lsla <- cluster_optimal(g_lsla)
oc_lss <- cluster_optimal(g_lss)

# output image
memb_hsla <- oc_hsla$membership
memb_hss <- oc_hss$membership
memb_lsla <- oc_lsla$membership
memb_lss <- oc_lss$membership

# evlaution
m_hsla <- modularity(oc_hsla,memb_hsla)
m_hss <- modularity(oc_hss,memb_hss)
m_lsla <- modularity(oc_lsla,memb_lsla)
m_lss <- modularity(oc_lss,memb_lsla)

# hsla
png("/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/r_image/2011/hsla_2011.png",width = 1080,height = 1080)
plot(oc_hsla,g_hsla,vertex.color = memb_hsla,
     vertex.label.cex = 1,
     edge.width = 0.01,
     edge.arrow.size=0.1,
     edge.arrow.width=0.05,
     )
dev.off()

# hss
png("/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/r_image/2011/hss_2011.png",width = 1080,height = 1080)
plot(oc_hss,g_hss,vertex.color = memb_hss,
     vertex.label.cex = 1,
     edge.width = 0.01,
     edge.arrow.size=0.1,
     edge.arrow.width=0.05,
)
dev.off()

# lsla
png("/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/r_image/2011/lsla_2011.png",width = 1080,height = 1080)
plot(oc_lsla,g_lsla,vertex.color = memb_lsla,
     vertex.label.cex = 1,
     edge.width = 0.01,
     edge.arrow.size=0.1,
     edge.arrow.width=0.05,
)
dev.off()

# lss

png("/Users/xuanlong/Documents/program/python/src/hansiqi/project/pro/experimentdata/r_image/2011/lss_2011.png",width = 1080,height = 1080)
plot(oc_lss,g_lss,vertex.color = memb_lss,
     vertex.label.cex = 1,
     edge.width = 0.01,
     edge.arrow.size=0.1,
     edge.arrow.width=0.05,
)
dev.off()

#fc <- cluster_edge_betweenness(g_hsla)
#plot(fc,g_hsla)

# zc <- cluster_fast_greedy(g_am)
# plot(zc,g_am)

