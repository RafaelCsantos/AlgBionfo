from Bio.SeqIO import parse 
from Bio.SeqRecord import SeqRecord 
from Bio.Seq import Seq 

file = open('exemplo.fasta') 

records = parse(file, "fasta") 

for i in records:    
   print("Id: %s" % i.id) 
   print("Name: %s" % i.name) 
   print("Description: %s" % i.description) 
   print("Annotations: %s" % i.annotations) 
   print("Sequence Data: %s" % i.seq) 

