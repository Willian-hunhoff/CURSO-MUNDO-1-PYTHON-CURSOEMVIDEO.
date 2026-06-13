cont = 1
while(cont == 1 ):
    salario = int(input('digite o valor que você recebe: '))
    if salario  > 1620:
        print('seu salario de {} teve um aumento de {:.2f} e agora é {:.2f}' .format(salario, salario * 0.10, salario *1.1))
    else:
        print('seu salario de {} teve um aumento de {:.2f} e agora é {:.2f}' .format(salario, salario*0.15, salario*1.15))
    cont = int(input('escreva 1 para repetir o codgio e 0 para sair '))
print('Adeus até a proxima! ') 