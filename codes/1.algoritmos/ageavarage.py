"""
Fazer um algoritmo que:
• Leia um número indeterminado de linhas
contendo cada uma a idade de um
indivíduo.
• A última linha que não entrará nos cálculos,
contém o valor da idade igual a zero.
• Calcule e escreva a idade média deste
grupo de indivíduos.
• Escreva também a maior idade e a menor

"""
keepdoing = True;
age =0 ;
counter =0;
while(keepdoing==True):
    num = float(input("Type your age:"))
    age +=num;
    if(num==0):
        keepdoing= False;
    else:
        counter+=1;
        num=0;

ageavarage = age/counter;

print("The age avarage is {}.".format(ageavarage));
    


