cont = 1
while( cont == 1 ):
    print('-='*20)
    print('analisador de triangulos')
    print('-='*20)
    print('')
    r1 = float(input('escreva o primeiro seguimento do triangulo '))
    r2 = float(input('escreva o segundo seguimento do triangulo '))
    r3 = float(input('escreva o terceito seguimento do triangulo '))
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('')
        for _ in range(5):
            print('...processando')
        print('')
        print('esses números podem formar um triangulo ')
        print('')
    else:
        print('')
        for _ in range(5):
            print('...processando')
        print('')
        print('nunca na vida q faz um triangulo')
        print('')
    cont = int(input('digite 1 para recomeçar e  0 para sair'))
    print('')