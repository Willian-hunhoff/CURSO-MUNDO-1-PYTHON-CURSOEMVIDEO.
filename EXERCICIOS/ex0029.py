cont = 1
while (cont == 1):
    kms = int(input('quantos km/h você estava? '))
    if kms > 80:
        multa = kms -80
        print('Você ultrapassou o limite de velocidade você deve pagar {} reais! ' .format(multa * 7))
    cont = int(input('digite 1 para recalcular e 0 para sair: '))