#11.Escreva um algoritmo para ler o salário mensal atual de um funcionário e 
#o percentual de reajuste. Calcular e escrever o valor do novo salário.
s = float(input('informe o salario: '))
a =  float(input('informe porcentagem de ajuste: '))
aj = s * a/100
print('o salario ajustado e R$' , round(s + aj , 2))


