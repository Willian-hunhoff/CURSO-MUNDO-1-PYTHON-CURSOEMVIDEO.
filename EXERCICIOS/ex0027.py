cont = 1
while (cont == 1):
    nome = str(input('escreva o seu nome: ')).strip()
    nome = nome.split()
    print ('prazer em te conhecer!')
    print('seu primeiro nome é {}' .format(nome[0]))
    print('seu ultimo nome é {}' .format(nome[len(nome) -1]))
    cont = int(input('digite 1 para continuar e 0 para sair '))
print('Adeus até a proxima ')