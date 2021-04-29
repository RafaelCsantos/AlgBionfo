import numpy as np
mat = np.random.randint(-5,5,(4,3) )
print(mat, "\n")

print("Valor absoluto",np.absolute(mat))
print("Seno dos valores da primeira linha",np.sin(mat[0,0:3]))
print("Valor máximo das colunas",mat.max(0))
print("Soma dos elementos da coluna",mat.sum(0))
print("Soma dos elementos em cada linha",mat.sum(1))



