cont = 1
while(cont == 1):
    num1 = float(input("digite a altura da sua parede: "))  
    num2 = float(input("digite a largura da sua parede: "))
    area = num1 * num2
    qtl = area / 2
    print("a area da sua parede é = a {}m² você precisara de {} litros de tinta para pinta-la " .format(area, qtl))
    cont = int(input("digite 1 para continuar calculando caso o contrario digite 0: "))
print("Adeus até a proxima!")