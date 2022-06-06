'''
5. Faça um programa que carregue uma matriz 2 x 3, calcule e mostre a quantidade de elementos da
matriz que não pertencem ao intervalo [5, 15].
'''
cont = 0
matriz=[[1,2,13],[10,14,15]]
for l in range(0,2):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
for l in range(0,2):
    for c in range(0,3):
        if matriz[l][c] < 5 or matriz[l][c]>15:
            cont = cont + 1
print('A matriz contém', cont, 'elementos fora do intervalo de 5 a 15')

