cont = 1
while(cont == 1):
    produto = float(input("digite o valor do produto para saber seu desconto de 5%: "))
    desc = float(produto * 0.95)
    print("o valor inicial do produto era de {:.2f}R$ com o desconto ele fica por {:.2f}R$" .format(produto, desc))
    cont = int(input("digite 1 para continuar fazendo calculos e 0 se deseja sair "))
print("Adeus até a proxima!")