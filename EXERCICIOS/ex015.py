cont = 1
while(cont ==1):
    dias = int(input("quantos dias o carro foi alugado? "))
    kmr = float(input("quantos kms o carro rodou?"))
    valor = (kmr * 0.15) + (dias * 60)
    print("se o carro foi usado por {} dias e rodou {}km o valor pago do aluguel sera de{}R$" .format(dias, kmr, valor))
    cont = int(input("digite 1 para repetir o codigo e 0 para sair"))
print("Adeus até a proxima!")