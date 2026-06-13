cont = 1
while(cont == 1):
    c = float(input("digite quantos graus C° deseja converter: "))
    f = ((9*c)/5)+32
    print("{}C° são {}Farenheint" .format(c, f))
    cont = int(input("digite 1 para repitir o codigo e 0 para sair: "))
print('Adeus até a proxima!')