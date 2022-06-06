# 14 .Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma 
#pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas: 
#para sexo masculino: peso ideal = (72.7 * altura) - 58 
#para sexo feminino: peso ideal = (62.1 * altura) - 44.7
input('informe o nome: ')
l = float(input('informe a altura: '))
print()
print('informe 1 para masculino ')
print('informe 2 para feminino ')
print()
op = float(input('informe a opçao: '))
if op == 1:
    p1 = (72.7 + l) - 58
    print('o peso ideal e ' , rounf(p1 , 2))
elif op == 2:
    p2 =(62.1 * l) - 44.7
    print('o peso ideal e ' , round(p2 , 2))
else:
    print('opção invalida ')
    
