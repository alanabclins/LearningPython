"""
Numa eleição existem três candidatos
identificados pelos números 1, 2 e 3.
Faça um algoritmo que compute o
resultado de uma eleição. Inicialmente o
programa deve pedir o número total de
votantes. Em seguida, deve pedir para
cada votante votar (informando o
numero do candidato) e ao final mostrar
o número de votos de cada candidato.
"""
candidato1 =0;
candidato2= 0;
candidato3 = 0;
vote=0;
eleitores= int(input("How many ellectors are going to be in this ellection?"));

for num in range (eleitores):
    vote=int(input("Who are you gonna vote: 1 , 2 or 3 ? Press enter to vote"))
    if (vote == 1 ):
        candidato1+=1;
    elif (vote ==2):
        candidato2+=1;
    else:
        candidato3+=1;
        
print("Candidato 1 : {}".format(candidato1))
print("Candidato 2 : {}".format(candidato2))
print("Candidato 3 : {}".format(candidato3))