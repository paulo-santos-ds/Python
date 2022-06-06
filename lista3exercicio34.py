# 34.Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.

i = 0
soma = 0
while i < 10:
    v = int(input('informe o valor: '))
    soma = soma + v
    i = i + 1;

print('a soma do valores e  :' , soma)
