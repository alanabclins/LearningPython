"""
Desenvolva um algoritmo que efetue a leitura
de três valores numéricos representando os lados
de um triângulo. O algoritmo deverá verificar e
informar se os lados fornecidos formam
realmente um triângulo (cada lado é menor que a
soma dos outros dois lados). Se esta condição for
verdadeira, deverá ser indicado qual tipo de
triângulo foi formado: isósceles (dois lados iguais
e um diferente), escaleno (todos os lados
diferentes) ou eqüilátero (todos os lados são
iguais).
"""
def formatriangulo(ladoA, ladoB, ladoC):
    if ladoA <= 0 or ladoB <= 0 or ladoC <= 0:
        return False
    if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
        return True
    else:
        return False
    
def tipoDoTriangulo (a, b, c):
        if a == b == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"

ladoA = float(input("Lado A size:"))
ladoB = float(input("Lado B size:"))
ladoC = float(input("Lado C size:"))

if(formatriangulo(ladoA,ladoB,ladoC)):
    print("Forma triangulo")
    print(tipoDoTriangulo(ladoA,ladoB,ladoC))
else:
    print("Não forma triangulo")
