''' Escreva um programa que leia números digitados. O
programa deve ler os números até que o usuário digite 0
(zero). No final da execução exiba a quantidade de
números digitados assim como a soma e a média
aritmética'''

qtd=0
soma=0
while True:
    num=float(input("digite o numero"))
    soma=soma+num
    qtd=qtd+1    
    if (num==0):
        break

    
print(qtd)
print(soma)

