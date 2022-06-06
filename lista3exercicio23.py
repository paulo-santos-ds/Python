#23.Construa um algoritmo que receba o preço de custo de um produto e 
#mostre o valor de venda. Sabe-se que o preço de custo receberá um 
#acréscimo de acordo com um percentual informado pelo usuário.
c = float(input('informe o preço de custo: '))
i = float(input(' informe o acrescimo em porcentagen: '))
pa = c * i/100 #acrescimo
pf = c + pa
print()
print('o valor final do produto e: ' , pf)
