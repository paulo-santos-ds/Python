#28.Um banco concederá um crédito especial aos seus clientes de acordo 
#com o saldo médio no último ano. Faça um programa que receba o saldo 
#médio de um cliente e calcule o valor do crédito, de acordo com a tabela 
#a seguir. Mostre o saldo médio e o valor do crédito.
#Acima de R$ 400,00-------------- 30% do saldo médio
#R$ 400,00 ------------ R$ 300,00 25% do saldo médio
#R$ 300,00 -------------R$ 200,00 20% do saldo médio
#Até R$ 200,00 -------------------10% do saldo médio

sm = float(input('informe o saldo medio: '))
if sm > 400:
    c = sm * 30/100
    print('o saldo medio e ' , sm , 'o credito e: ' , c)
elif sm <= 400 and sm >= 300:
    c = sm * 25/100
    print('o saldo medio e ' , sm , 'o credito e ' , c)
elif sm >= 200 and sm < 300:
    c = sm *20/100
    print('o saldo medio e ', sm , 'o valor do credito e ' , c)
else:
    sm < 200
    c = sm * 10/100
    print(' o saldo medio e ' , sm , 'o valor do credito e ' , c)
