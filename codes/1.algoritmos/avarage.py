#Ler três notas de um aluno, calcular a média e
#informar se ele foi aprovado (Média ≥ 7), reprovado
#(Média < 7) ou aprovado com louvor (Média = 10)

grade1 = float(input("Test grande one: "));
grade2 = float(input("Test grande two: "));
grade3 = float(input("Test grande three: "));

avarage = (grade1 + grade2 + grade3)/3;

if(avarage==10):
    print("Approved with honor")
elif(avarage>=7):
    print("Approved")
else: 
    print("Try again")


