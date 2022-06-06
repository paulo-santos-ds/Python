#22.Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres 
#(considere que as idades dos homens serão sempre diferentes entre si, 
#bem como as das mulheres). Calcule e escreva a soma das idades do 
#homem mais velho com a mulher mais nova, e o produto das idades do 
#homem mais novo com a mulher mais velha.

h1 = int(input('informe a idade do primeiro homem: '))
h2 = int(input('informe a idade do segundo homem: '))
m1 = int(input('informe a idade da primeira mulher: '))
m2 = int(input('informe a idade da segunda mulher: '))

if h1 > h2:
    if h1 > h2 and m1 > m2:
        print('a soma de idade homem mais velho e mulher nais nove', h1 + m2)
        print(h2 * m1)
    else:
        h1 > h2 and m2 > m1
        print('a soma de idade homem mais velho e mulher nais nove', h1 + m1)
        print('produto das idades do homem mais novo com a mulher mais velha' , h2 * m2)
else:
    h2 > h1
    if h2 > h1 and m1 > m2:
        print('a soma de idade homem mais velho e mulher nais nove', h2 + m1)
        print('produto das idades do homem mais novo com a mulher mais velha' , h2 * m2)
    else:
        h2 > h1 and m2 > m1
        print('a soma de idade homem mais velho e mulher nais nove', h2 + m1)
        print('produto das idades do homem mais novo com a mulher mais velha' , h1 * m2)

    

    
 












