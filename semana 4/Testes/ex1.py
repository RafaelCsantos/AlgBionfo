'''Desenvolva um programa que solicite o primeiro número
de uma PA e sua razão. O programa deve imprimir os 10
primeiros termos. '''

termo=int(input("digite o primeiro termo da PA"))
razao=float(input("Digite a razao da PA"))
cont=0

print ("o 1º termo é", termo)

for i in range (9):

    i=termo+razao
    cont=cont+1
    print("O",cont+1, " Termo é ", i)
    termo=i



