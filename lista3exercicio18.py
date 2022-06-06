#18.Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
n1 = int(input('informe o primeiro numero: '))
n2 = int(input('informe o segundo numero: '))
n3 = int(input('informe o terceiro numero: '))

if n1 > n2:
    if n1 > n2 and n2 > n3:
        print('a soma dos dois maiores e ' , n1 + n2)
    elif n1 > n2 and n2 < n3:
        print('a soma dos dois maiores e ' , n1 + n3)
elif n2 > n3:
    if n2 > n3 and n3 > n1:
        print('a soma dos dois maiores e ' , n2 + n3)
    elif n2 > n3 and n3 < n1:
        print('a soma dos dois maiores e ' , n2 + n1)
else:
    n3 > n1
    if n3 > n1 and n1 > n2:
        print('a soma dos dois maiores e ' , n3 + n1)
    elif n3 > n1 and n1 < n2:
        print('a soma dos dois maiores e ' , n3 + n2)

 






























    
    
         


