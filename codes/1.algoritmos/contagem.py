alturas = [1.70, 1.65, 1.80, 1.60, 1.75, ...] 
sexos = [0, 1, 0, 1, 1, ...]  

maior_altura = alturas[0]
menor_altura = alturas[0]
soma_altura_mulheres = 0
num_homens = 0
num_mulheres = 0

for i in range(len(alturas)):
    if alturas[i] > maior_altura:
        maior_altura = alturas[i]
        
    if alturas[i] < menor_altura:
        menor_altura = alturas[i]
    
    if sexos[i] == 1:
        soma_altura_mulheres += alturas[i]
        num_mulheres += 1
    else:
        num_homens += 1

if num_mulheres > 0:
    media_altura_mulheres = soma_altura_mulheres / num_mulheres
else:
    media_altura_mulheres = 0
total_pessoas = len(alturas)
porcentagem_homens = (num_homens / total_pessoas) * 100
porcentagem_mulheres = (num_mulheres / total_pessoas) * 100
print("Maior altura: {:.2f}".format(maior_altura))
print("Menor altura: {:.2f}".format(menor_altura))
print("Média de altura das mulheres: {:.2f}".format(media_altura_mulheres))
print("Número de homens: {}".format(num_homens))
print("Porcentagem de homens: {:.2f}%".format(porcentagem_homens))
print("Porcentagem de mulheres: {:.2f}%".format(porcentagem_mulheres))