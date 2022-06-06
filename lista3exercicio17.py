# 17 .Faça um programa que receba dois números e execute uma das 
#operações listadas a seguir de acordo com a escolha do usuário. Se for 
#digitada uma opção inválida mostrar mensagem de erro e terminar o 
#programa. As opções são: 
#• Média entre os dois números. 
#• Diferença do maior pelo menor. 
#• produto entre os dois números.
n1 = float(input('informe o primeiro numero: '))
n2 = float(input('informe o segundo numero: '))
print('digite opçao 1 para media: ')
print('digite opção 2 para diferença maior pelo menor: ')
print('digite opção 3 produto dos dois numero: ')
n = int(input('informe a opção: '))
if n == 1:
    n3 = (n1 + n2)/2
    print('a media e: ' , round(n3 , 2 ))
    
elif n == 2:
    print('opção 2 selecionado')
    if n1 > n2:
        print(' diferença do maior pelo menor: ' , n1 - n2)
    elif n2 > n1:
      print('a diferença maior numero pelo menor e' , n2 -n1)
    else:
      print('os numeros sao iguais')
elif n == 3:
  print('o produto entre dois numeros e: ' , n1 * n2 ) 
else:
  n > 3
  print('opção invalida')

