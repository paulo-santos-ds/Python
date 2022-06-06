# 4. Uma empresa decide dar um aumento de 30% aos funcionários com 
#salários inferiores a R$ 500,00. Faça um programa que receba o salário 
#do funcionário e mostre o valor do salário reajustado ou uma mensagem, 
#caso o funcionário não tenha direito ao aumento.

s = float(input('informe o salario: '))
if s < 500:
    sa = s *30/100 # ajuste do salario
    print('o salario ajustado e: ' , round(s + sa , 2))
else:
    print('funcionario não tem direito ao reajuste de salario')











