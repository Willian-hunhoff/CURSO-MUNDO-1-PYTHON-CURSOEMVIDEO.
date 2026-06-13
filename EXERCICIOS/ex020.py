from random import shuffle
al1 = input("qual o nome do primeiro aluno? ")
al2 = input("qual o nome do segundo aluno? ")
al3 = input("qual o nome do terceiro aluno? ")
al4 = input("qual o nome do quarto aluno? ")
lista = [al1, al2, al3, al4]
shuffle(lista)
print("a lista sorteada sera")
print(lista)