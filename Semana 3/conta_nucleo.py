#receber sequencia
sequencia=input("Digite uma sequência de DNA")
sequencia=sequencia.upper()
#verificar se sequencia é valida
for i in sequencia:
    if i in 'ATCG':
         continue
    else:
     print("sequencia invalida. O Programa vai se encerrar")
    exit()

print("sequencia válida \n")

#b)imprimir o número total de nucleotídeos nasequência

total=(len(sequencia))
print("Quantidade total: ",total, "\n")

#C)Calcular e imprimir a quantidade de cada um
qtda=(sequencia.count('A'))
qtdt=(sequencia.count('T'))
qtdc=(sequencia.count('C'))
qtdg=(sequencia.count('G'))
print("Adeninas (A)",qtda, "\n", "Citosinas (C)",qtdc,"\n", "Timinas (C)",qtdt,"\n", "Guaninas (G)",qtdg,"\n")


#D)Calcular e imprimir a frequencia (%) de cada um dos nucleotideos
print("Frequencia de A",(qtda/total)*100, "%")
print("Frequencia de T",(qtdt/total)*100, "%")
print("Frequencia de C",(qtdc/total)*100, "%")
print("Frequencia de G",(qtdg/total)*100, "%")