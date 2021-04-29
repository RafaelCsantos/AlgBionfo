seqa=open('seq_a.fasta','r')
seqb=open('seq_b.fasta','r')
seqa.readlines(1)
seqb.readlines(1)
lista1=seqa.read().replace("\n","")
lista2=seqb.read().replace("\n","")


dif=0


for i in range (0,200):
  if (lista1[i]) != (lista2[i]) :
    print("A posicao : ",i+1,"Foi trocado",lista1[i],"-- >",lista2[i])
    dif=dif+1
      
print("O numero de nucleotideos diferentes é",dif)


