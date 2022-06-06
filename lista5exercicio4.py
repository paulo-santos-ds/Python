'''
4. Construa um programa que preencha, de forma automática (dentro do código), duas matrizes de
números inteiros. Calcule a diferença entre os elementos das duas matrizes e armazene o
resultado em uma terceira matriz. Percorrer a matriz resultante exibindo os elementos.
'''
matriz1 =[[4,5,9],[3,4,9],[7,8,5]]
matriz2 =[[2,4,8],[3,8,9],[6,7,7]]
print('    matriz1   \n')
for l in range(0, 3):
    for c in range(0, 3):
         print(f'[{matriz1[l][c]:^4} ]', end='')
    print()
print()
print('-----subtrair-------\n')
                  
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]:^4} ]', end='')
    print()
print()
print('-----resultado-------')
print()
for l in range(0,3):
    for c in range(0,3):
        matriz1[l][c] = matriz1[l][c] - matriz2[l][c]
        print(f'[{matriz1[l][c]:^4}]', end='')
    print()

        
 