'''
8. Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva todos os
elementos, exceto os elementos da diagonal principal.
'''
matriz = [[10,0,0,0,0,0,0,0,0,0],[0,20,0,0,0,0,0,0,0,0],
          [0,0,30,0,0,0,0,0,0,0],[0,0,0,40,0,0,0,0,0,0],
          [0,0,0,0,50,0,0,0,0,0],[0,0,0,0,0,60,0,0,0,0],
          [0,0,0,0,0,0,70,0,0,0],[0,0,0,0,0,0,0,80,0,0],
          [0,0,0,0,0,0,0,0,90,0],[0,0,0,0,0,0,0,0,0,100]]

for l in range(0, 10):
    for c in range(0, 10):
        if matriz[l][c]==matriz[l][c]:
            matriz[l][l]=''       
for l in range(0, 10):
    for c in range(0, 10):
        print(f'[{matriz[l][c]:^3}]', end='')
       
    print()
print()