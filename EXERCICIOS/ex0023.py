cont = 1
while(cont == 1):
    num = int(input('escreva um número de 0 a 9999: '))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('unidade:', u)
    print('dezena:', d)
    print('centena:', c)
    print('milhar:', m)
    cont = int(input('escreva 1 para recomeçar o codigo e 0 para sair '))
print("Adeus até a proxima!")
