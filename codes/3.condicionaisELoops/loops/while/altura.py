def contar(alunos):
    alunos_abaixo_15 =0;
    for idade, altura in alunos:
            if idade > 13 and altura < 1.5:
                alunos_abaixo_15 += 1

    return alunos_abaixo_15

alunos = []
while True:
    try:
        idade = int(input("Digite a idade do aluno (digite 0 para parar): "))
        if idade == 0:
            break
        altura = float(input("Digite a altura do aluno: "))
        alunos.append((idade, altura))
    except ValueError:
        print("Valor inválido! Por favor, digite um número inteiro válido.")
resultado = contar(alunos)
print("Quantidade de alunos com mais de 13 anos e altura inferior a 1.5: ", resultado)
