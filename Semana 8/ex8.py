from Bio.Blast import NCBIXML 
from Bio import SeqIO

seqs=[]

#A) imprimindo sequencia B
for sequencia in SeqIO.parse("lista_blast.fasta", format="fasta"):
 seqs.append(sequencia)
print(seqs[1])

#B)Blastn, pois a sequência fasta é de nucleotídeos, sendo BLastn a ferramenta mais adequada pra esse tipo de análise

#C) Criação do XML

#D) Imprimir sequencia, tamanho, score e gaps com scores acima de 40
arquivo_xml = open("blast_resultado.xml","r")
dados = NCBIXML.parse(arquivo_xml)
item = next(dados)
i=1
for a in item.alignments:
 
    for hsp in a.hsps:
        if hsp.score>40:
        
            print("Alinhamento",i)
            print("Tamanho",a.length)
            print("Score:",hsp.score)
            print("Gaps:",hsp.gaps)
            i+=1



#Análise dos Resultados:
#D) Qual o organismo que pertence as sequencias? 
'''A sequência A, está com resultados próximos a um gene de Halobacterium salinarum.
A Sequencia B, está com resultados próximos a um gene presentes em raízes, com grandes correspondencias entre uma proteína antifungica em Raphanus sativus e similar a alguma proteina de Brassica rapa  
A sequencia C, está relacionada a  amylase 1 de Mus musculus
A sequencia D, está relacionada a uma neurotoxina II de Androctonus  Australis
A sequencia E, está relacionada a Streptococcus pyogenes. '''

#E) Cite a identificação do genbank que melhor alinha a sequência. 
'''Sequencia A - M24774.1
Sequencia B - U18557.1
Sequencia C - U90136.1
Sequencia D - M27704.1
Sequencia E - LS483352.1'''

#F)Cite o trabalho na qual está envolvido a sequência do item e. 
'''CONSRTM   Pathogen Informatics
  TITLE     Direct Submission
  JOURNAL   Submitted (08-JUN-2018) WTSI, Pathogen Informatics, Wellcome Trust
            Sanger Institute, CB10 1SA, United Kingdom'''


