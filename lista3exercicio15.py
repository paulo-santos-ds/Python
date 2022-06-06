# 15 .Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma 
#empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total 
#das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, 
#calcular e escrever o seu salário total.
s = float(input('informe o salario: '))
v1 = float(input('informe o valor das vendas efetuadas: '))
c1 = v1 * 3/100# comissao 3%
v2 = 1500 - v1 #excedente
c2 = v2 * 5/100 #comissao acima de 1500 venda 5%
if v1 >= 0 and v1 <= 1500:
    print('o salario total e: ',  round(s + c1 , 2))
elif v1 > 1500:
    print('o salario total e: ' , round(s + c1 + c2  , 2))
else:
    print('valor das vendas invalidas ')

    













