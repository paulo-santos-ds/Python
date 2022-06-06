'''
10. Faça um programa que carregue uma matriz 3 x 3 com números reais e receba um valor, número
digitado pelo usuário, calcule e mostre a matriz resulte da multiplicação do número digitado por
elemento da matriz

'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]

print()
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=(int(input(f'informe um numero[{l},{c}]:')))       
print()
for l in range(0,3):
   for c in range(0,3):
       print(f'[{matriz[l][c]:^3}]', end='')
   print()
       

print()
n = int(input('informe o multiplicador: '))
x = [[n,n,n],[n,n,n],[n,n,n]]
print()
print('----nova matriz-----')

print()
for l in range(0,3):
   for c in range(0,3):
       
       matriz[l][c] = matriz[l][c] * x[l][c]
       print(f'[{matriz[l][c]:^3}]', end='')
   print()
   

    
    
 
         



