# install.packages('cluster')
# install.packages('factoextra')

library(cluster)
library(factoextra)
library(tidyverse)

setwd("C:/Users/dande/Documents/Projects/spotiPylot/data")
df <- read.csv('pcaDF.csv')

df <- df %>% scale(center=TRUE, scale=TRUE)

clusters <- fanny(x=df, k=2, metric = 'SqEuclidean', memb.exp = 1.6)

clusters$membership
clusters$clustering
clusters$objective
clusters$k.crisp
clusters$coeff
clusters$convergence
clusters$diss
clusters$silinfo

p <- fviz_cluster(clusters, ellipse.type = "norm", repel=TRUE,
             palette = "jco", ggtheme = theme_minimal(),
             legend = "right")+geom_point(overlap, colour='r')

overlap <-clusters$membership[(clusters$membership[,1]<.60) & (clusters$membership[,2]<.60)]

subset(clusters$data, clusters$membership==overlap )

clusters$membership


plot(clusters)
clusters$clustering[clusters$clustering >1]
