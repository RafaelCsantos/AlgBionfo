maior=0
menor=0
ficha=list()
cont=0
soma=0

while True:

    nome=str(input('nome'))
    nota=float(input('nota da P1:') )
    
    menor=nota
    
    if (nota>0 and nota<=menor):
        menor=nota
    else:
        menor=menor
      
  
    if (nota>0 and nota>=maior):
        maior=nota
    else:
        maior=maior
        
    ficha.append([nome,nota])
    cont=cont+1
    soma=soma+nota
    resp=str(input("quer continuar? S/N"))
    if resp in 'Nn':
        break


#letra A
print("foram cadastrados ",cont, "alunos")

#letra B
for i,a in enumerate(ficha):
    if (a[1]>=maior):
        print("O aluno com a maior nota foi ",a[0], "com a nota de", a[1])

#letra C
for i,a in enumerate(ficha):
    if (a[1]<=menor):
        print("O aluno com a menor nota foi ",a[0], "com a nota de", a[1])

      

#Letra D
media= soma/cont
print("A media da sala foi de ",media)



    