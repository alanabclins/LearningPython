lista= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#intervalo de 1 a 9
print(lista[1:9])
#intervalo de 8 a 13
print(lista[8:13])
#numeros pares
for i in lista:
    if(i%2==0):
        print(i)
#múltiplo de 2, 3 e 4 
for i in lista:
    if i % 2 == 0 or i % 3 == 0 or i % 4 == 0:
        print(i)
# lista reversa
lista.reverse();
print(lista)  
lista.reverse();
#razao da som do intervalo de 10 a 15 prlo intervalo de 3 a 9 em float
dezaquinze = float(sum(lista[10:15]));
for i in lista[3:9]:
    dezaquinze=dezaquinze/i;
print(dezaquinze)
        