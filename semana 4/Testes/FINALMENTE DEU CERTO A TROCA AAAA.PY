output = open('teste4.txt','w')
entrada= open('teste1.txt','r')

for i in entrada :
    output.write(i.replace('A','t').replace("T","a").replace("C",'g',).replace("G",'c').upper() ) 

output.close()
