# 24 .Uma agência bancária possui dois tipos de investimentos, conforme o 
#quadro a seguir. Faça um programa que receba o tipo de investimento e 
#o valor do investimento e que calcule e mostre o valor corrigido de acordo 
#com o tipo de investimento.
# poupança 3%
#fundo de renda fixa 4%
p = 3/100 #poupaça 3%
f = 4/100 # fundo de renda fixa 4%
print('Para investimento em poupança digite    1 ')
print('para investimento em renda fixa digite  2 ')
print()
op = int(input('informe o tipo de investimento desejado: '))
print()

if op == 1:
    print('opçao desejada poupança')
    d = float(input('informe o valor do investimento: '))
    dr = d * p
    print('o valor corrigido para poupança foi R$ ' , round(d + dr , 2))
elif op == 2:
    print('opção desejada fundo de investimento renda fixa')
    d = float(input('informe o valor do investimento: '))
    dr = d * f
    print('o valor corrigido para fundo de renda fixa foi R$ ' , round(d + dr , 2))
else:
    print('opção invalida')
    
    
    








