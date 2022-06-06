# 10 As maçãs custam R$ 1,30 cada se forem compradas menos de uma 
#dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um 
#programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
p1 = 1.3
p2 = 1.00
n = int(input('informe a quantidade de maçãs: '))
if n < 12:
    print('o valor da compra e R$ ' , n * 1.3)
else:
    print('o valor da compra e R$ ' , n)
