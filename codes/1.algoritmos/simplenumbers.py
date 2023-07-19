#Determinar se um número é par ou ímpar e positivo ou negativo

num= int(input("Type the number that you need to study"));
text= " ";
if(num>0): 
    text=" is even";
else:
    text=" is odd";

if(num%2==0):
    text+= " and positive.";
else:
    text+= " and negative.";
    
print("The number {} {}".format(num,text));



