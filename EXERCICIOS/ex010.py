cont = 1
while(cont ==1):
    real = float(input("digite quantos reais você tem para fazer a conversão Obs: Utilize ponto ao invez de virgula caso o numero seja quebrado "))
    dol = float(real / 3.27)
    print("com {:.2f}R$ Voçê pode comprar {:.2f}U$ dolares" .format(real, dol))
    cont = int(input("digite 1 para continuar o codigo e 0 para sair: "))
print("Adeus até a proxima!")