"""
3. Crie um programa que cadastre
informações de várias pessoas (nome,
idade e cpf) e depois coloque em um
dicionário. Depois remova todas as
pessoas menores de 18 anos do
dicionário e coloque em outro dicionário.
"""

dicionario_maiores = { "nome": "","idade": 0,"cpf": 0}
dicionario_menores = {}

nome= str(input("Nome "))
age= int(input("Idade "))
cpf= int(input("cpf "))

dicionario_maiores = [nome, age, cpf]

if(age<18):
    dicionario_menores = [nome, age, cpf]
    delete = dicionario_maiores.pop("nome")
    delete= dicionario_maiores.pop("age")
    delete = dicionario_maiores.pop("cpf")
    
print(dicionario_maiores)
print(dicionario_menores)


