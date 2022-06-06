# 33 .Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.
i = 0
contador = 0
v = 0 # valor inserido
while i < 10:
    
    v= int(input('informe um numero: '))
    if(v <0):
        contador = contador + 1
        
    i = i +1;
    
print('existe ' , contador , 'numeros negativos')
       
