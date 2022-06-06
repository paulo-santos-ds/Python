'''
2. Na teoria dos sistemas, define-se o elemento MINMAX de uma matriz como o maior elemento da
linha em que se encontra o menor elemento da matriz. Elabora um programa que carregue uma
matriz 4 x 7 com números reais, calcule e mostre seu MINMAX e sua posição (linha e coluna).
'''
posicoes  = []
#matriz = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
maior = -999999
menor = 9999999
matriz = [[1,2,3,4,5,60,7],[11,12,13,14,15,20,25],[30,32,33,35,36,37,100],[57,59,54,56,-60,62,66]]
'''
for l in range(0,4):
    for c in range (0,7):
        matriz[l][c] = int(input(f'informe um numero[{l},{c}]:'))
print()
'''
for l in range(0,4):
    for c in range(0,7):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print()
menor = matriz[0][0]
l_maior =0
for l in range(0,4):
    for c in range(0,7):
        if matriz[l][c]< menor:
            menor = matriz[l][c]
            posicoes=[(l,c)]
            l_menor = l
maior = matriz[l_menor][0]
c_maior = 0
for c in range(0,7):
    if matriz[l_menor][c]> maior:
        maior = matriz[l_menor][c]
        c_maior = c
print('o menor valor da matriz e', menor, 'fica na posicao',posicoes)
print(f' posicao minimax esta com valor maior da linha', maior, 'na posicao',[(l_menor,c_maior)])