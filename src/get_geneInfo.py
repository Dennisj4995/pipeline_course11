import sys
import mygene

class get_functions():
    idlist="RNA-Seq-test.txt"
    
    def __init__(self):
        self.get_id()

    def get_id(self):
        mg = mygene.MyGeneInfo()
        with open("output/geneInfo.txt", 'w') as gi:
            gi.write("tag"+"\t"+"id"+"\t"+"symbol"+"\t"+"name")
            gi.write("\n")
            with open(self.idlist) as ids:
                next(ids)
                for line in ids:
                    line=line.split('\n')[0]
                    tag=line.split('\t')[0]
                    search= mg.query(tag, size=1)
                    #print(search)
                    hits=search.values()[0]
                    name=hits[0].values()[0]
                    symbol=hits[0].values()[2]
                    id=hits[0].values()[5]
                    info=tag + "\t"+ id +"\t"+symbol+"\t"+name
                    gi.write(str(info))
                    gi.write("\n")
                    #print(hits)

if __name__ == '__main__':
    start = get_functions()