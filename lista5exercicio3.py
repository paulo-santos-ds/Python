'''
3. Faça um programa que calcule e mostre a media dos elementos da diagonal principal de uma
matriz 10 x 10.
'''
x= 0
matriz=[[10,0,0,0,0,0,0,0,0,0],[0,201,0,0,0,0,0,0,0,0],
        [0,0,100,0,0,0,0,0,0,0],[0,0,0,400,0,0,0,0,0,0],
        [0,0,0,0,5,0,0,0,0,0],[0,0,0,0,0,6,0,0,0,0],
        [0,0,0,0,0,0,7,0,0,0],[0,0,0,0,0,0,0,80,0,0],
        [0,0,0,0,0,0,0,0,90,0],[0,0,0,0,0,0,0,0,0,110]]
       
for l in range(0, 10):
    for c in range(0, 10):
        if matriz[l][c] == matriz[l][c]:
            x = x + matriz[l][c]           
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
print()
media = x /10
print('a soma dos elementos da diagonal principal e ', x )
print('a media dos elementos da diagonal principal e ', round(media,2))




