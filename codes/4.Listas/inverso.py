"""
Ler uma lista de 10 números reais e

mostre-os na ordem inversa.
"""
lista = []
for i in range (10):
    lista.append(int(input(f"Digite o número {i+1} da lista : ")))
    
lista.reverse()
print(lista);
