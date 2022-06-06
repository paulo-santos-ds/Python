# 13.A jornada de trabalho semanal de um funcionário é de 40 horas. O 
#funcionário que trabalhar mais de 40 horas receberá hora extra, cujo 
#cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um 
#algoritmo que leia o número de horas trabalhadas em um mês, o salário 
#por hora e escreva o salário total do funcionário, que deverá ser acrescido 
#das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
s1 = float(input('informe o salario: '))
h = int(input('informe o numero de horas trabalhadas no mes: '))
ph = s1 / 220 # valor da hora trabalhada
he = ph * 1.5 # valor da hora extra 50%
if h > 0:
    print('o salario total com hora extras e R$ ' , round( s1 + h*he, 2))
else:
    print('funcionario não tem hora extra seu salario e R$' , round( s1 , 2))













