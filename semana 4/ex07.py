entrada= open('Corona_genomic.fasta','r')
saida= open('ex07_a','w')

entrada.readlines(1)


for i in entrada.readlines():
    saida.write(i.replace('A','t').replace("T","a").replace("C",'g',).replace("G",'c').upper() ) 

entrada.close()
saida.close()

entrada= open('Corona_genomic.fasta','r')
saida=open('coronaux.txt','w')
entrada.readlines(1)

for i in entrada.readlines():
    saida.write(i.replace('A','u').replace("T","u").replace("C",'g',).replace("G",'c').upper() )
    
entrada.close()
saida.close()

saida=open('coronaux.txt','r')

for i in saida.readlines() :
    print(i)







    


