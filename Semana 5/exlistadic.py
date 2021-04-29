soma=0
media=0
pessoa={}
galera=[]
while True:
    pessoa.clear()
    pessoa['nome'] =str(input('Nome:'))
    pessoa['sexo']= str(input('Sexo')).upper()
    pessoa['idade']=int(input('Idade'))
    soma=soma+pessoa['idade']
    galera.append(pessoa.copy())
    resp=str(input("Deseja continuar?"))
    
    if resp==('N'):
        break



print("a quantidade de pessoas cadastradas foi de",len(galera))
print("a media é de",soma/len(galera))

