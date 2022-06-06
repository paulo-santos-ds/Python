'''
9. Criar um algoritmo que carregue uma matriz 12 x 4 com os valores das vendas de uma loja, em
que cada linha represente um mês do ano, e cada coluna, uma semana do mês. Para fins de
simplificação considere que cada mês possui somente 4 semanas. Calcule e
imprima:
• Total vendido em cada mês do ano;
• Total vendido em cada semana durante todo o ano;
• Total vendido no ano.
'''
soma = 0
soma_semana1=0
soma_semana2=0
soma_semana3=0
soma_semana4=0

meses = [["mes/semana"," 1° semana","2°semana","3°semana","4° semana"],
         ["janeiro",1200, 1300, 1600,1700],["Fevereiro" ,1900, 1751, 2300,2321],
         ["Março" , 2500, 2400, 1900,1980], ["Abril", 2400, 2200, 1600,1799],
         ["Maio" ,  2350, 2710, 1951,1454], ["Junho", 2943, 2200,  1807,1200],
         ["Julho" ,  2650, 2830, 1654,1778],["Agosto", 2140, 2007,  1120,1748],
         ["Setembro", 2350, 2710, 1951,1922], ["Outubro", 2961, 2471,  1723,1921],
         ["Novembro" ,  2450, 2610, 1121,1741], ["Dezembro", 1943, 2600,  3120,4100]
         
         ]
for l in range(0,13):
    for c in range(0,5):
        print(f' {meses[l][c]:^10}', end='')
    print()
print()    
for l in range(1,13):
    soma_mes = 0
    for c in range(1,5):
        soma = soma + meses[l][c]
        soma_mes += meses [l][c]
    print(f'o total de vendas durante o mes de {meses[l][0]:^10} R$' , soma_mes)
print()
for l in range(1,13):
            soma_semana1 += meses[l][1]
print('a soma da primeira semana de todos os meses e R$' , soma_semana1)
for l in range(1,13):
            soma_semana2 += meses[l][2]
print('a soma da segunda  semana de todos os meses e R$' , soma_semana2)
for l in range(1,13):
            soma_semana3 += meses[l][3]
print('a soma da terceira semana de todos os meses e R$' , soma_semana3)
for l in range(1,13):
            soma_semana4 += meses[l][4]
print('a soma da quarta semana de todos os meses   e R$' , soma_semana4)        
print()
print('o total de vendas durante o ano e R$' , soma)




