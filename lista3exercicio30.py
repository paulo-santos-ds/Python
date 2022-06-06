#30.Ler dois valores e imprimir uma das três mensagens a seguir: 
#• ‘Números iguais’, caso os números sejam iguais 
#• ‘Primeiro é maior’, caso o primeiro seja maior que o segundo; 
#• ‘Segundo maior’, caso o segundo seja maior que o primeiro.
n1 = float(input('informe o primeiro numero: '))
n2 = float(input('informe o segundo numero: '))
if n1 > n2:
    print('o primeiro numero e maior: ')
elif n2 > n1:
    print('o segundo numero e maior: ')
else:
    n1 == n2
    print('os numeros são iguais: ')