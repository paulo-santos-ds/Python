# 2. O custo ao consumidor de um carro novo é a soma do custo de fábrica 
#com a percentagem do distribuidor e dos impostos (aplicados, primeiro os 
#impostos sobre o custo de fábrica, e depois a percentagem do distribuidor 
#sobre o resultado). Supondo que a percentagem do distribuidor seja de 
#28% e os impostos 45%. Escrever um algoritmo que leia o custo de fábrica 
#de um carro e informe o custo ao consumidor do mesmo.

pf = float(input('informe o preço de fabricação R$ '))
tf = pf * 28/100
td = pf * 45/100
print('o custo do carro ao consumidor final e R$ ' , round(pf + tf + td , 2))













