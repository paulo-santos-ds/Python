# 21 Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#Álcool até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro

#Gasolina até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro

#Escreva um algoritmo que leia o número de litros vendidos e o tipo de 
#combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule 
#e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro 
#da gasolina é R$ 6,30 e o preço do litro do álcool é R$ 4,90.
pa = 4.9
pg = 6.3
print('informe o combustivel a ser abastecido: ')
print()
print('para alcool digite ...  A  ')
print('para gasolina digite .. G  ')
print()

op = input('informe a opção  ' )
if op == 'A' :
    q = int(input('informe a quantidade de alcool a ser abastecido: '))
    if q <= 20:
        ta = q * pa
        da = pa * q * 3/100 # desconte de 3 % alcool ate 20 litros
        
        print('o total de alcool a ser pago e: ' , round(ta - da , 2))
    elif q > 20:
        ta = q * pa
        da = pa * q * 5/100 # desconte de 5 % alcool acima de 20 litros
        print('o total de alcool a ser pago e: ' , round(ta - da , 2))
    else:
        q <= 0
        print('quantidade de combustivel invalida')
elif op == 'G':
    q = float(input('informe a quantidade de Gasolina a ser abastecido: '))
    if q <= 20:
        tg = q * pg
        dg = pg * q * 4/100 # desconto de 4 % ate 20 litros de gasolina
        print('o total de gasolina a ser pago e: ' , round(tg - dg , 2 ))
    elif q > 20:
        tg = q * pg
        dg = pg * q * 6/100 # desconto de 6 % acima de 20 litros de gasolina
        print('o total de gasolina a ser pago e: ' , round(tg - dg , 2) )
    else:
        q <= 0
        print('opçao invalida')
else:
    print('opção invalida')
        
        
    














