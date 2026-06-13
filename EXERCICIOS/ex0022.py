nome = input("escreva seu nome completo ").strip()
print ("o seu nome completo é: {}" .format(nome))
print("o seu nome com todas as letras maiusculas fica {}" .format(nome.upper()))
print("seu nome escrito inteiramente em minusculo fica {}" .format(nome.lower()))
print("o seu nome tem um total de {} caracteres sem contar os espaços" .format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras .format(nome.find(' ')))
nome = nome.split()
print(print("o seu primeiro nome é {} e tem {} caracteres" .format(nome[0], len(nome[0]))))


