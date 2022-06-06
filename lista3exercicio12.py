# 12 .Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma 
#mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

i = int(input('informe o ano de nascimento: '))
v = 2021 - i
if v >= 16:
    print('podera votar sua idade e ' , v , 'anos' )
else:
    print('nao poderar votar sua idade ' , v , 'anos')









