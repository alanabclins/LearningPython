"""
Ler uma lista com 4 notas, em seguida
o programa deve exibir as notas e a
média.
"""
notas =[]
for i in range(4):
    notas.insert(i,float(input(f"Nota {i+1} ")))
min= min(notas)
max= max(notas)
media= (sum(notas)/len(notas))

print(f"Nota mínima", min, " Nota maxima ", max, " Media ",media)