# 25 .Faça um algoritmo para ler: a descrição do produto (nome), a quantidade 
#adquirida e o preço unitário. Calcular e escrever o total (total = quantidade 
#adquirida * preço unitário), o desconto e o total a pagar (total a pagar = 
#total - desconto), sabendo-se que: 
#• Se quantidade <= 5 o desconto será de 2% 
#• Se quantidade > 5 e quantidade <=10 o desconto será de 3% 
#• Se quantidade > 10 o desconto será de 5%
n = input('informe o nome do produto: ')
q = int(input('informe a quantidade: '))
p = float(input('informe o preço unitario: '))
print()

if q <= 5:
    d1 = 2/100
    t = q * p
    d = t * d1
    print('o preço total da fruta: ' , n , round(t , 2) )
    print('o desconto de ' , n ,  round( d , 2))
    print('o valor a ser pago na fruta: ', n , round(t - d , 2))
elif q > 5 and q <= 10:
    d1 = 3/100
    t = q * p
    d = t * d1
    print('o preço total da fruta: ' , n ,round( t , 2) )
    print('o desconto de ' , n ,  round( d , 2))
    print('o valor a ser pago na fruta: ', n , round(t - d , 2))
else:
    q > 10
    d1 = 5/100
    t = q * p
    d = t * d1
    print('o preço total da fruta: ' ,'R$' , n , round(t , 2) )
    print('o desconto de ' , n , 'R$', round( d , 2))
    print('o valor a ser pago na fruta ', n , 'R$', round(t - d , 2))
    
    
       

