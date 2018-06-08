#source("https://bioconductor.org/biocLite.R")
#biocLite("KEGGREST")
library(KEGGREST)
setwd("~/Desktop/School/pipeline_course11/src")
cnts <- read.delim("../RNA-Seq-test.txt")
#row.names(cnts) <- cnts[,"ID"]
x<-NULL
kegg.table<-data.frame(id=NULL, info=NULL)
for (l in cnts$ID){
  query<- keggGet(c(paste("lpl:",l,sep="")))
  if ("ORTHOLOGY" %in% names(query[[1]])) {
  y<-query[[1]]$ORTHOLOGY
  k<-names(query[[1]]$ORTHOLOGY)
  }
  else {
    y<-"NA"
    k<-"NA"
  }
  if ("PATHWAY" %in% names(query[[1]])) {
    path<-paste(names(query[[1]]$PATHWAY),query[[1]]$PATHWAY)
    #for (p in query[[1]]$PATHWAY){
    for (p in path){
      x<-paste(x,p,sep=" ")
    }
  }
  else { x<-"NA"}
  id_table <- data.frame(id=l,ko=k,orthology=y,pathway=x)
  x<-NULL
  kegg.table <- rbind(kegg.table,id_table)
}

write.table(kegg.table, file = "../output/kegg.txt",sep="\t",quote = FALSE,row.names=FALSE)

