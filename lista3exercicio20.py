# 20 .Ler o nome de 2 times e o número de gols marcados na partida (para cada 
#time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE

t1 = int(input('informe a quantidade de gol marcado pelo time 1: '))
t2 = int(input('informe a quantidade de gols marcados pelo time 2: '))
if t1 > t2:
    print('time 1 vencedor com: ' , t1 , 'gols')
elif t2 > t1:
    print('time 2 vencedor com: ' , t2 , 'gols')
else:
    print('EMPATE')










