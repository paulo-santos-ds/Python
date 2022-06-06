# 19 .Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média 
#aritmética simples e escrever uma mensagem que diga se o aluno foi ou 
#não aprovado (considerar que nota igual ou maior que 6 o aluno é 
#aprovado). Escrever também a média calculada.

n1 = float(input('informe a primeira nota: '))
n2 = float(input('informe a segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('o aluno foi aprovado com a media: ' , m)
else:
    print('Aluno reprovado media: ' , m)