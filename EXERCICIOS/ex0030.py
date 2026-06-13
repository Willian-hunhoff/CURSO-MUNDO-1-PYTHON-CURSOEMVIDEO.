cont = 1
while (cont == 1):
    num = int(input('digite um número para saber se ele é par ou impar: '))
    if num % 2 == 0:
        print('o número {} é par! ' .format(num))
    else:
        print('seu número é impar!')
    cont = int(input('escreva 1 para recomeçar e 0 para sair '))
print('Adeus até a proxima!')