cont = 1
while(cont == 1):
    ano = int(input('escreva um ano para descobrir se ele é bissexto: '))
    if ano % 4 == 0:
        print("seu ano é bissexto")
    else:
        print('seu ano nao é bissexto')
    cont = int(input('escreva 1 para recomeçar e 0 para sair '))
print('Adeus até a proxima! ')