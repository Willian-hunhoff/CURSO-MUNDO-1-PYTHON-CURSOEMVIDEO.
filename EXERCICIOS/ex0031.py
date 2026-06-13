cont = 1
while (cont == 1):
    kms = int(input('quantos kms tera sua viagem? '))
    if kms <= 200:
        #preço por km 50 centavos
        print('você ira gastar {} R$ de passagem pois a viagem é curta' .format(kms * 0.5))
    else:
        #preço por km 45 centavos
        print('você ira gastar {} R$ de passagem pois a viagem é longa' . format(kms * 0.45))
    cont = int(input('escreva 1 para recomeçar e 0 para sair '))
print('Adeus até a proxima! ')