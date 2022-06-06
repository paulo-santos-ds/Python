# 7. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, 
#meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
i = int(input('informe a idade em anos: '))
m = int(input('numero de meses: '))
n = int(input('numero de dias: '))

ni = i * 365
nm = m * 30
print('o numero de dias que a pessoa vive desde o nascimento e: ' , ni + m + n)