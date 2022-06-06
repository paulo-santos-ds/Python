#27.Faça um algoritmo para ler um número que é um código de usuário. Caso 
#este código seja diferente de um código armazenado internamente no 
#algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário 
#inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a 
#senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada 
#a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser 
#mostrada a mensagem ‘Acesso permitido’.
u = 1234
su = 9999

n = int(input('informe o numero de usuario: '))
if n == u:
    s = int(input('informe a senha de usuario: '))
    if s == su:
        print('ACESSO PERMITIDO')
    else:
        print('senha incorreta')
else:
    print('usuario invalido')