from Bio import SeqIO
from Bio import Entrez
class get_sequence():
    idlist="RNA-Seq-test.txt"

    def __init__(self):
        self.get_identiefiers()
        self.get_pubmed()
        self.sort_id()
        self.write_file()

        
    def get_identiefiers(self):
        tags=""
        with open(self.idlist) as ids:
                next(ids)
                for line in ids:
                    line=line.split('\n')[0]
                    tag=line.split('\t')[0]
                    tags=tags+"\t"+tag
        self.tags=tags.split()
    def get_pubmed(self):
        Entrez.email = "mail@mail.com"
        id_list = []
        for single_term in self.tags:
            data = Entrez.esearch(db="pubmed",term = single_term)
            res = Entrez.read(data)
            pmids = res["IdList"]
            if pmids ==[]:
                found= single_term + "\t" + "NA"
                id_list.append(found)
            elif not pmids ==[]:
                found= single_term
                for i in pmids:
                    found = found + "\t" + i
                id_list.append(found)
        self.id_list=id_list

    def sort_id(self):
        id_list=self.id_list
        id_list.sort(key=len)
        self.sorted_list=id_list

    def write_file(self):
        pubmed=self.sorted_list
        with open("output/pubmedids.txt", 'w') as out:
            for i in pubmed:
                out.write(i + "\n")
if __name__ == '__main__':
    start = get_sequence()