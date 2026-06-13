cont = 1
while( cont == 1 ):
    num1 = int(input('escreva o primeiro número '))
    num2 = int(input('escreva o segundo número '))
    num3 = int(input('escreva o terceiro número '))
    maior = num1
    if num2 > num1 and num2 > num3:
        maior = num2
    if num3 > num1 and num3 > num2:
        maior = num3
    menor = num1
    if num2 < num3 and num2 < num1:
        menor = num2
    if num3 < num2 and num3 < num1:
        menor = num3
    print('o menor número é {} ' .format(menor))
    print('o maior número é {} ' .format(maior))
    print('')
    cont = int(input('escreva 1 para recomeçar e 0 para sair '))
print('Adeus até a proxima! ')
    