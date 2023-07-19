"""
Anacleto tem 1,50m e cresce 2
centímetros por ano, enquanto
Felisberto tem 1,10 e cresce 3
centímetros por ano. Construa um
programa que calcule e apresente
quantos anos serão necessários para
que Felisberto seja maior que
Anacleto.
"""
ano =0;
anacleto = 1.50;
taxaAnacleto = 0.02;
felizberto = 1.10;
taxaFelizberto = 0.03;
while(felizberto<=anacleto):
    anacleto+=taxaAnacleto;
    felizberto+=taxaFelizberto;
    ano+=1;

print("Quantidade de anos {}".format(ano))