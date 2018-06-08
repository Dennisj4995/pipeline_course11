import re
class write_report():
    
    idlist="RNA-Seq-test.txt"
    geneinfo="output/geneInfo.txt"
    pubmed="output/pubmedids.txt"
    kegg="output/kegg.txt"
    sequences="output/sequences.txt"
    def __init__(self):
        self.get_identifiers()
        self.get_function()
        self.get_pubmed()
        self.get_kegg()
        self.get_seq()
        self.write_report()
    def get_identifiers(self):
        tags=""
        with open(self.idlist) as ids:
            next(ids)
            for line in ids:
                line=line.split('\n')[0]
                tag=line.split('\t')[0]
                tags=tags+"\t"+tag
        self.tags=tags.split()

    def get_function(self):
        functestlist=[]
        with open(self.geneinfo) as inf:
            next(inf)
            for line in inf:
                ide=line.split("\t")[1]
                symbol=line.split("\t")[2]
                function=line.split("\t")[3]
                functest="ID: "+ide+"\n"+"Symbol: "+symbol+"\n"+"Function: "+function
                functestlist.append(functest)
        self.functestlist=functestlist
        #print(functestlist)

    def get_pubmed(self):
        pubmedlist=[]
        with open(self.pubmed) as pmd:
            for line in pmd:
                pmdid=re.sub(r"lp_....","", line)
                pubmedlist.append(pmdid)
        self.pubmedlist=pubmedlist

    def get_kegg(self):
        kegglist=[]
        with open(self.kegg) as kegg:
            next(kegg)
            for line in kegg:
                ko = line.split("\t")[1]
                ortho = line.split("\t")[2]
                path = line.split("\t")[3]
                keggy="KO: "+ko+"\n"+"Orthology: "+ortho+"\n"+"Pathways: "+path
                kegglist.append(keggy)
        self.kegglist=kegglist

    def get_seq(self):
        sequ=""
        with open(self.sequences) as seq:
            copy = False
            for line in seq:
                if line.strip():
                    sequ=sequ+line
            seqlist=sequ.split(">")
            seqlist.pop(0)
            self.seqlist=seqlist

        
    def write_report(self):
        with open("Gene_report.txt", "w") as out:
            i=0
            for t in self.tags:
                #for t in self.functestlist:
                    #for s in self.seqlist[1]:
                out.write("Tag: "+t)
                out.write("\n")
                out.write(self.functestlist[i])
                out.write("Pubmed ID: "+self.pubmedlist[i])              
                out.write(self.kegglist[i])
                out.write("\n")
                out.write(self.seqlist[i])
                out.write("\n")
                out.write("\n")
                i=i+1



if __name__ == '__main__':
    start = write_report()