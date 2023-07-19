"""
Ler uma lista de 5 números inteiros e
mostre cada número juntamente com a
sua posição na lista.
"""
lista = []
for i in range (5):
    lista.append(int(input("Digite o número da lista : ")))

for i,p in enumerate(lista):
    print(f"Indice {i+1} e elemento {p} ")

