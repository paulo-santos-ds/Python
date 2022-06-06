# 3.Faça um programa que receba três números e mostre o maior.
n1 = float(input('informe um numero: '))
n2 = float(input('informe o segundo numero: '))
n3 = float(input('informe o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('o primeiro numero e maior: ' , n1)
    
elif n2 > n1 and n2 > n3:
    print('o segundo numero e maior: '  , n2)
    
else:
    print ('o terceiro numero e maior: ', n3)
  
         

