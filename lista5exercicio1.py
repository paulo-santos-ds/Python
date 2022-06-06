'''
1. A tabela abaixo identifica as temperaturas máximas, médias e mínimas registradas em cada
estação do ano de 2014 em uma cidade qualquer.
• A estação com a menor temperatura máxima
• A estação com a maior temperatura média
• A estação com a maior temperatura mínima
• A estação com a menor temperatura mínima
• A estação com a maior temperatura maxima
'''
v= [0,0,0,0,0]
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
metma = 9999#menor temperatura maxima
matme = -9999 #maior temperatura media
matmi = -9999 #maior temperatura minima
metmi = 9999 #menor temperatura minima
matma = -9999 #maior temperatura maxima
matriz = ["Primavera",27,25,22],["Verao",31,26,23],["outono",25,24,19],["inverno",24,22,16]
v =["Estacao"],["maxima"],["Media"],["Minima"]

print(v)
for l in range(0,4):
    for c in range(0,4):                                                                                                     
        print(f'[{matriz[l][c]:^10}]', end='')
    print()
print()
# A estação com a menor temperatura máxima
for l in range(0,4):
    if l ==0:
        metma = matriz[l][1]
    elif matriz[l][1] < metma:
        metma = matriz[l][1]
        esta_1 = matriz[l][0]
print(f'A menor temperatura maxima e ', metma,'°C na estação ' , esta_1)
# A estação com a maior temperatura média
for l in range(0,4):
    if l ==0:
        matme = matriz[l][2]
    elif matriz[l][2] > matme:
        matme = matriz[l][2]
        esta_2 = matriz[l][0]
print(f'A maior temperatura media  e ' , matme,'°C na estação ' , esta_2)
# A estação com a maior temperatura mínima
for l in range(0,4):
    if l ==0:
        matmi = matriz[l][3]
    elif matriz[l][3] > matmi:
        matmi = matriz[l][3]
        esta_3 = matriz[l][0]
print(f'A maior temperatura minima e ', matmi,'°C na estação ' , esta_3)
# A estação com a menor temperatura mínima
for l in range(0,4):
    if l ==0:
        metmi = matriz[l][3]
    elif matriz[l][3] < metmi:
        metmi = matriz[l][3]
        esta_4 = matriz[l][0]
print(f'A menor temperatura minima e ', metmi,'°C na estação ' , esta_4)
# A estação com a maior temperatura maxima
for l in range(0,4):
    if l ==0:
        matma = matriz[l][1]
    elif matriz[l][1] > matma:
        matma = matriz[l][1]
        esta_5 = matriz[l][0]
print(f'A maior temperatura maxima e ', matma,'°C na estação ' , esta_5)






