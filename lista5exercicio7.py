'''
7. Faça um programa que carregue uma matriz 3 x 5 com números inteiros, calcule e mostre a
quantidade de elementos entre 15 e 20
'''
matriz =[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]

for i in range(0,3):
    for j in range(0,5):
        matriz[i][j] = int(input(f'informe um numero[{i},{j}]:'))
    
#contar range
cont= 0
for i in range(0,3):
    for j in range(0,5):
        if matriz[i][j] >=15 and matriz[i][j]<=20: 
            cont = cont + 1
#imprimir em formato de matriz
for i in range(0,3):
    for j in range(0,5):
        print(f'[{matriz[i][j]:^4}]', end='')
    print()
#imprimir qtde de números pares
print()
print('A matriz contém', cont, 'números no intervalo de 15 a 20 ')
