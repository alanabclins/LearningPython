"""
Algoritmo que calcule e escreva a soma dos 50 primeiros termos de uma série explicado no exercício
"""
numero = 1000;
divisor= 1;
contador =0;
resultadoconta=0;
resultadototal=0;

while(contador<50):
    resultadoconta=numero/divisor;
    if(divisor%2==0):
        resultadototal -= resultadoconta
    else:
        resultadototal += resultadoconta
    numero-=3
    divisor+=1
    contador+=1


print("Resultado total {}".format(resultadototal)) 