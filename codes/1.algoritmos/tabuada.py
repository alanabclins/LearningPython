"""
Construa um programa que exiba
a tabuada de 1 até N.
"""
n = int(input("Final da tabuada é: "))

def exibir_tabuada(n):
    for num in range(1, int (n)+1):
        print(f"Tabuada do {num}:")
        for i in range(1, 10 +1):
            resultado = num * i
            print(f"{num} x {i} = {resultado}")
        print()  # Linha em branco entre as tabuadas
        

exibir_tabuada(n);

