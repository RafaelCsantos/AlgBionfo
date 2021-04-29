""" Faça um programa que calcule a soma os números
impares e múltiplos de 3 que se encontram no intervalo
de 1 até 500"""
soma=0

for i in range ((500)+1) :
    if (i%1==0 and i%3==0):
        soma=soma+(i)

print(soma)

