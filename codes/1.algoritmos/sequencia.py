"""
Fazer um algoritmo para calcular
e escrever a seguinte soma:
37x38/1 + 36x37/2 + 35x36/3 + ... +
1x2/37
"""
primeiro=37;
segundo=38;
denominador=1;
resultadoparcial=0;
resultadototal=0;
while(denominador<=37):
    resultadoparcial=(primeiro*segundo)/denominador;
    resultadototal+=resultadoparcial;
    primeiro-=1;
    segundo-+1;
    denominador+=1;

print(f"Resultado = {resultadototal}")