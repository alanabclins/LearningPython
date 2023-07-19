"""
Ler o valor de um cheque e escrever o quanto

vai ser recolhido de CPMF. Considere que
imposto recolhe uma taxa de 0,3%. Imprimir
o valor do imposto.
"""
cheque= float(input("Valor cheque: "))
imposto = cheque * 0.3 ;
print(f"{imposto}")