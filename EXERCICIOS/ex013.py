cont = 1
while(cont == 1):
    sal = float(input("digite seu salario para calcular seu aumento de 15% "))
    salau = float(sal + sal * 15/100 )
    print("o seu salario de {:.2f}R$ aumentou para {:.2f}R$ Parabens! " .format(sal, salau))
    cont = int(input("digite 1 para continuar calculando e 0 para sair "))
print("Adeus até a proxima!")