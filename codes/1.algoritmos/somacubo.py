"""
Fazer um algoritmo para calcular e
escrever a soma dos cubos dos
números pares compreendidos entre
B e A (B > A). B e A são lidos pelo
teclado.
"""

a = int(input("Type the number A: "))
b = int(input("Type the number B: "))

sum_of_cubes = 0

for num in range(a, b + 1):
    if num % 2 == 0:
        cube = num ** 3
        sum_of_cubes += cube

print("The sum of cubes of even numbers between {} and {} is {}".format(a, b, sum_of_cubes))

    