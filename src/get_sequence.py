from Bio import SeqIO
from Bio import Entrez
class get_sequence():
    idlist="RNA-Seq-test.txt"

    def __init__(self):
        self.get_identifiers()
        self.get_entrez()
        self.write_file()
    ##knipt alle ID's uit de count file
    def get_identifiers(self):
        tags=""
        with open(self.idlist) as ids:
                next(ids)
                for line in ids:
                    line=line.split('\n')[0]
                    tag=line.split('\t')[0]
                    tags=tags+"\t"+tag
        self.tags=tags.split()

    def get_entrez(self):
        Entrez.email = "mail@mail.com"
        seq_list = []
        for term in self.tags:
            ##Zoekt de juiste ID's met ID's uit count file
            handle = Entrez.esearch(db="gene", term=term ,retmode="text",retmax=1)
            record = Entrez.read(handle)
            id=record["IdList"][0]
            id=id
            ##Zoekt in de gene database naar de genen
            handle = Entrez.efetch(db="gene", id=id ,rettype="text", retmode="text", retmax=1)
            record = handle.read()
            splt = record.split("\n")[4]
            ##accessie code voor de complete sequentie
            acc=splt.split()[1]
            ##knipt seq start en stop positie voor elk gen zodat deze uit de complete sequentie kunnen
            ##worden geknipt
            seqstart=splt.split()[2].split("..")[0].replace("(", "")
            seqstop=splt.split()[2].split("..")[1].replace(")", "")
            if "," in seqstop:
                seqstop= seqstop.replace(",","")
            #print(seqstart)
            #print(seqstop)
            ##haalt de nucleotide sequentie op
            handle = Entrez.efetch(db="nuccore", id=acc ,rettype="fasta", seq_start=seqstart, seq_stop=seqstop)
            record = handle.read()
            seq=record.replace(record.split('\n', 1)[0],">"+term)
            seq_list.append(seq)
            # with open("sequences/"+term+"_seq.txt", "w") as out:
            #     out.write(record)
        #with open("sequences/"+term+"_seq.txt", "w") as out:
            #out.write(record)
        self.seq_list=seq_list
    ##schrijft de nucleotide sequenties weg naar een lijst
    def write_file(self):
        sequences=self.seq_list
        with open("output/sequences.txt", "w") as out:
            for i in sequences:
                out.write(i)

if __name__ == '__main__':
    start = get_sequence()