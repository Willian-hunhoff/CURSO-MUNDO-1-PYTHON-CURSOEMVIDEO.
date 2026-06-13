cont = 1
while (cont == 1):
    import random
    num = random.randrange(1, 6)
    adivinhar = int(input('adivinhe o número de 1 a 5 que o computador esta pensando '))
    if adivinhar == num:
        print('parabens você acertou!')
    else:
        print('burro')
    cont = int(input('escreva 1 para recomeçar e 0 para sair '))