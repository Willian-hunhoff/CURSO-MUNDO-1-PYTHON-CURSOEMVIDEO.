nome = "-"
cont = 1
while(cont == 1):
    num1 = float(input("digite o número que você deseja saber a tabuada "))
    x2 = num1 * 2
    x3 = num1 * 3
    x4 = num1 * 4
    x5 = num1 * 5
    x6 = num1 * 6
    x7 = num1 * 7
    x8 = num1 * 8
    x9 = num1 * 9
    x10 = num1 * 10
    print ("-" * 20)
    print("{} x 1 é = {}" .format(num1, num1 ))
    print("{} x 2 é = {}" .format(num1, x2))
    print("{} x 3 é = {}" . format(num1, x3))
    print("{} x 4 é = {}" . format(num1, x4))
    print("{} x 5 é = {}" . format(num1, x5))
    print("{} x 6 é = {}" . format(num1, x6))
    print("{} x 7 é = {}" . format(num1, x7))
    print("{} x 8 é = {}" . format(num1, x8))
    print("{} x 9 é = {}" . format(num1, x9))
    print("{} x 10 é = {}" . format(num1, x10))
    print ("-" * 20)
    cont = int(input("se deseja saber outra tabuada digite 1 se deseja sair do programa digite 0: "))
print("Adeus até a proxima!")