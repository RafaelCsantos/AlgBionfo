pessoas = list()
pessoa = dict()
resp = 'S'
s_peso = peso_medio = 0
s_altura = altura_media = 0
s_IMC = IMC_medio = 0
while resp=='S':
    pessoa.clear()
    pessoa['nome'] = str(input('Qual o nome? '))
    pessoa['sexo'] = str(input('Qual o sexo?(M/F) '))
    pessoa['peso'] = float(input('Qual o peso?(em kg) '))
    pessoa['altura'] = float(input('Qual a altura?(em metros) '))
    pessoa['IMC'] = pessoa['peso']/(pessoa['altura']*pessoa['altura'])
    pessoas.append(pessoa.copy())
    resp = str(input('Quer continuar?(S/N) '))
    s_peso += pessoa['peso']
    s_altura += pessoa['altura']
    s_IMC += pessoa['IMC']
peso_medio = s_peso / len(pessoas)
altura_media = s_altura / len(pessoas)
IMC_medio = s_IMC / len(pessoas)
print(f'O número de pessoas é: {len(pessoas)}')
print(f'O peso médio é: {peso_medio:.2f}')
print(f'A altura média é: {altura_media:.2f}')
print(f'O IMC médio é: {IMC_medio:.2f}')
