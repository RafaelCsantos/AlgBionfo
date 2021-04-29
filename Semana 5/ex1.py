def main(n1):
    
    fat = 1
    i = 2
    while i <= n1:
        fat = fat*i
        i = i + 1

    print("O valor de %d! é =" %n, fat)

#-----
n = int(input("Digite o valor do número: "))
main(n)
