
n=int(input())
lista=[]

if  1<=n<=100:
    for i in range (n):
        valor=int(input())
        lista.append(valor)

print(max(lista))
