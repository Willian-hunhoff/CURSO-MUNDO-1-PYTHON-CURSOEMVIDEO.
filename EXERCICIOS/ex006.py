cont = 1
while(cont == 1):
    num = int(input("escrea seu número para receber o dobro o triplo e sua raiz quadrada: "))
    d = num*2
    t = num*3
    r = num**(1/2)
    print("o dobro é = a {} o triplo é = a {} e a raiz quadrada é {}" .format(d, t, r))
    cont = int(input("digite 1 para continuar com o mesmo codigo e 0 para sair "))
print("Adeus até a proxima!")