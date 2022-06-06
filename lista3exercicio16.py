# 16 .Faça um algoritmo para ler: número da conta do cliente, saldo, débito e 
#crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito 
#+ crédito). Também testar se saldo atual for maior ou igual a zero escrever 
#a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.
c = input('informe o numero da conta do cliente: ')
s = float(input('informe o saldo: '))
d = float(input('informe o valor do debito: '))
cr = float(input('informe o valor do credito: '))
sa = s - d + cr
if sa >= 0:
    print('saldo positivo')
else:
    print('Saldo negativo')













