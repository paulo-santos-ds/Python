#29.Uma empresa quer verificar se um empregado está qualificado para a 
#aposentadoria ou não. Para estar em condições, um dos seguintes 
#requisitos deve ser satisfeito: 
# Ter no mínimo 65 anos de idade. 
# Ter trabalhado no mínimo 30 anos. 
# Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
#Com base nas informações acima, faça um algoritmo que leia: o número 
#do empregado (código), o ano de seu nascimento e o ano de seu ingresso 
#na empresa. O programa deverá escrever a idade e o tempo de trabalho 
#do empregado e a mensagem 'Requerer aposentadoria' ou 'Não 
#requerer'.
c = input('informe o codigo do funcionario: ')
n = int(input('informe ano de nascimento:'))
i = int(input('informe ano ingresso a empresa: '))
print()
idade = 2021 - n
tt = 2021 - i #tempo de serviço
if idade >= 65 and tt > 30:
    print('a idade e' , idade , 'anos ,o tempo de trabalho e ' , tt , 'anos')
    print('funcionario' , c , 'Requer Aposentadoria: ')
elif idade >= 60 and tt >= 25:
    print('a idade e' , idade , 'anos , o tempo de trabalho e ' , tt , 'anos')
    print('funcionario' , c , 'Requer Aposentadoria: ')
    
else:
    print('a idade e' , idade , 'anos , o tempo de trabalho e ' , tt , 'anos')
    print('não Requer aposentadoria')


