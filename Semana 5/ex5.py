dados={}
pessoas=[]
peso=0
imc=0
altura=0
imctotal=0
cont=0
alttotal=0
pesototal=0
while True:
    
    pessoas.clear()
    dados['nome']= str(input('Nome:'))
    while True:
        dados['sexo']= str(input('Digite o Sexo M OU F:')).upper()
        if dados['sexo'] in 'MF':
            break
        print("Digite apenas M OU F")
    dados['peso']= float(input('Peso:'))
    peso=peso+dados['peso']
    pesototal=pesototal+peso
    dados['altura']= float(input('altura:'))
    altura=altura+dados['altura']
    alttotal=altura+alttotal
    cont=cont+1
    imc=round (peso/(altura**2),2)
    imctotal=round((imctotal+imc),2)
    imc=0
    altura=0
    peso=0
    pessoas.append(dados.copy())
    
    resp=str(input("Deseja continuar? N-não / Outra tecla - sim")).upper()

    if resp==("N"):
        break

print("A quantidade de pessoas cadastradas foi de",cont)
print("O peso médio das pessoas é de",pesototal/cont)
print("A altura media das pessoas é de",alttotal/cont)
print("O IMC médio das pessoas foi de",imctotal/cont)
