import random

def criar_matriz(tamanho):
    matriz = []
    for _ in range(tamanho):
        linha = [random.randint(1, 100) for _ in range(tamanho)]
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    try:
        tamanho = int(input("Informe o tamanho da matriz: "))
        if tamanho <= 0:
            print("O tamanho da matriz deve ser maior que zero.")
            return

        matriz = criar_matriz(tamanho)
        imprimir_matriz(matriz)
    except ValueError:
        print("Por favor, insira um número válido para o tamanho da matriz.")

if __name__ == "__main__":
    main()
