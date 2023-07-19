"""Ler a temperatura de uma pessoa e exibir a
mensagem “Febre Alta” (temp ≥ 39), “Febril”
(39 > temp ≥ 37) ou “Sem Febre” (temp
<

"""
temperatura = float(input("Temperature: "))

if(temperatura>= 39):
    print("Febre alta")
elif(temperatura < 39 and temperatura >= 37): 
    print("Febre")
else:
    print("Sem febre")