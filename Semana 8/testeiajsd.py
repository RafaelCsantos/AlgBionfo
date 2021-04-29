from Bio.Blast import NCBIXML 
#sequencia, tamanho, score e gaps

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



