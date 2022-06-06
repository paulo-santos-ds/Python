# 1 .Faça um algoritmo que receba o valor de um depósito e o valor da taxa
#de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento.

d = float(input('informe o valor do deposito R$ '))
j = float(input('informe a taxa de juros: '))
r = d * j/100
vt = d + r
print('o valor do montante total e R$ ' , round(vt , 2))