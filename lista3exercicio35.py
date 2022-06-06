# 35 Faça um algoritmo para ler uma quantidade e a seguir ler esta quantidade  de números.
#Depois de ler todos os números o algoritmo deve apresentar  na tela o maior dos números lidos e a média dos números lidos.

maior = -999999999
i= 0
soma = 0
numero = int(input('informe quantidade de vezes sera repetido: '))
while i < numero:
    v = int(input('informe o valor: '))
    #soma = soma + v
    #media = soma / numero
    if (v > maior):
        maior = v
    i = i + 1;
    soma = soma + v
    media = soma / numero  
print('o numero maior e: ', maior)

print('a smedia  e  :' , round(media, 2))
