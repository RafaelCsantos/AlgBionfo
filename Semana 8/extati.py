n= int(input())
lst=[]

if  1<=n<=100:
    for i in range (n):
        v= int(input())
        lst.append(v)

else:
    print('intervalo errado')

print(max(lst))

