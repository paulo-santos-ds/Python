# 9. Uma revendedora de carros usados paga a seus funcionários vendedores
#um salário fixo por mês, mais uma comissão também fixa para cada carro 
#vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um 
#algoritmo que leia o número de carros por ele vendidos, o valor total de 
#suas vendas, o salário fixo e o valor que ele recebe por carro vendido. 
#Calcule e escreva o salário final do vendedor.

s = float(input('informe o salario: '))
c = int(input('informe a quantidade de carros vendidos: '))
vc = float(input('informe valor total de carros vendidos: '))
co = c * vc * 5/100
print('o salario final e ' , s + co)















