"""
Entrar com um distância (km) e o tempo de
viagem (horas) de um automóvel, e dizer se
a velocidade média foi superior ao limite
(110 km/h) ou não.
"""
distancia = float(input("Distancia km :"))
hora = float(input("Distancia h :"))
media = distancia/hora;

if(media>110):
    print("Superior")
else:
    print("Inferior")