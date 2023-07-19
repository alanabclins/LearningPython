"""
Faça um Programa que peça para entrar com
um ano (inteiro com 4 dígitos) e determine se
o mesmo é ou não bissexto (divisível por 4).
"""
ano = int(input("Ano : "))

if(ano%4 == 0):
    print("Bissexto")
else:
    print("Regular")