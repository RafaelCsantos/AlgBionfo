""" Escreva um programa que pergunte o deposito inicial e a
taxa de Juros de uma poupança. Exiba os valores mês a
mês para os 24 primeiros meses. No final deve imprimir o
total de ganho com juros no período."""


di=float(input ("Digite o valor do deposito inicial"))
tx=float(input("digite a taxa de juros"))
cont=0
ganho=0

for i in range (24) :
    i=di+(di*tx)
    cont=cont+1
    ganho=(ganho+(i-di))
    
    print("Mes",cont, "valor",i)
    di=i



print ("O ganho total no periodo foi de ",ganho)




