cont = 1
while(cont ==1):
    num = int(input("escreva um numero para saber seu antecessor e seu sucessor "))
    a = num - 1
    s = num + 1
    print("seu antecessor é {} e seu sucessor é {}" .format(a, s))
    cont = int(input("digite 1 para repitir o codigo e 0 para sair "))
print("Adeus até a proxima!")