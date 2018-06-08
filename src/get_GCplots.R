#install.packages("seqinr")
library("seqinr")
setwd("~/Desktop/School/pipeline_course11/src")
dir.create("../output/gcplots")
fastafile<-read.fasta("../output/sequences.txt")
winsize = 50

for (sequence in fastafile) {
  
  starts = seq(1, length(sequence) - winsize, by = winsize)
  n = length(starts)
  chunkGCs = numeric(n)
  
  for (i in 1:n) {
    chunk = sequence[starts[i]:(starts[i]+winsize)]
    chunkGC = GC(chunk)
    chunkGCs[i] = chunkGC
  }
  pdf(file = paste('../output/gcplots/plot-', attr(sequence, 'name'), '.pdf', sep = ''))
  plot(starts, chunkGCs, type='b')
  dev.off()
  #print(paste(attr(sequence, 'name'), ' done'))
}
