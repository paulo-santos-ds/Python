'''
6. Construa um algoritmo que receba uma matriz D 5x5 (considere que não tenha valores
duplicados). A seguir ler um número X e escreva uma mensagem indicando se o valor de X existe
ou NÃO na matriz.'''
cont = 0
matriz = [[6,7,8,9,77],[75,74,96,81,72],[20,21,22,23,28],[91,92,93,86,45],[46,47,48,49,50]]
print()
for l in range(0,5):
    for c in range(0,5):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
x =int(input('informe um numero para comparação: '))
for l in range(0,5):
    for c in range(0,5):
        if matriz[l][c] == x:
            cont= cont + 1
if cont >0:
    print(f'o numero {x} esta na matriz')
else:
    print(f'o numero {x} não esta na matriz')
    
            
            
            










'''
for l in range(0,5):
    for c in range(0,5):  
        if (matriz[l][c] == x):
            if (matriz[l][c] == x):
                t=matriz[l][c]
                print(f'o numero' ,t,'esta na lista')
            else:
                False
                matriz[l][c] != x
                print('nao esta na lista')
            break
        
'''
    
       
    
   
  
           
       
    

      
            
        
        