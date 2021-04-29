qtdkm=float(input("Digite a quantidade de kms rodados \n") )
qtdias=int(input("Digite a quantidade de dias que o carro esta alugado \n"))

print("o Carro foi alugado por",qtdias,"dias \n e andou por ",qtdkm,"km \n")
print("o preço total foi de ",(qtdkm*0.15) + (qtdias*60), "reais" )

