cont = 1
while(cont ==1):
    num1 = float(input("digite a primeira nota do aluno: "))
    num2 = float(input("digite a segunda nota do aluno: "))
    media = float((num1+num2)/2)
    print("a media de {} com {} é = a: {}" .format(num1, num2, media))
    cont = int(input("digite 1 para repetir e 0 para sair"))
print("Adeus até a proxima!")
