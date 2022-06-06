# 26.Crie um programa onde o usuário informe os valores dos catetos de um 
#triângulo e que ao final mostre a sua hipotenusa. De acordo com o 
#teorema de Pitágoras, toda hipotenusa é constituída pela soma dos 
#quadrados de cada cateto. Sendo assim, a fórmula mais conhecida para 
#o cálculo da hipotenusa é a seguinte: a² + b² = c²
b = float(input('informe o valor do cateto oposto: '))
a = float(input('informe o valor do cateto adjacente: '))
c = a*a + b*b
d = c**0.5
print('o calculo da hipotenusa e: ' , round(d , 2 ))






