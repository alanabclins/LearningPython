"""
8. Número primo é aquele que só é
divisível por ele mesmo e pela
unidade. Fazer um algoritmo que
determine e escreva os números
primos compreendidos entre um
intervalo fornecido pelo usuário.
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

prime_numbers=[];

start = int(input("Define start number: "))
end = int(input("Define end number: "))

for num in range (start, end):
    if (is_prime(num)):
        prime_numbers.append(num);


print(prime_numbers)
