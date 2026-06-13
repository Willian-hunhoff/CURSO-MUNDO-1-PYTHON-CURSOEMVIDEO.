frase = 'curso em video'
print(frase)
#escreve a frase
print(frase[:12:2])
#escreve a partir do inicio de 2 em 2
print (frase[7:])
#escreve apartir do 7
print (frase[0::3])
#pula de 3 em 3
print (len(frase))
#conta quantos espaços tem
print(frase.count('o'))
#conta quantas letras o tem
print(frase.count('o', 0, 11))
#conta quantos ós tem entre 0 e 11
print(frase.find('video'))
#acha onde começa a palavra nos espaços
print(frase.find('android'))
#retorna o valor -1 se nao tiver essa string na variavel
print('curso' in frase)
print('bosta' in frase)
#escreve se tem a string na variavel
frase = frase.replace('video', 'legal')
#substitui as palavras na variavel
print(frase.replace('video', 'legal'))
print(frase.upper())
#deixa tudo em maiusculo
print(frase.lower())
#deixa tudo em minusculo
print(frase.capitalize())
#deixa toda a frase em minuscula e depois deixa so a primeira maiuscula
print(frase.title())
#deixa em maiusculo toda letra apos um espaço
print('bosta' in frase)
#procura a palavra na frase
print(frase.replace('legal', 'bosta'))
# troca uma palavra pela outra
print(frase.find('bosta'))
#procura uma palavra na string
print(frase.split())
#divide uma cadeia de palavras na string em varias strings por exemplo curso 1 em 2 video 3
print("""skadjklajwlkdjisajldwa
      dsadsaljdaskljldsa
      fasljdskajkldasjk
      jdlaskdjasdlsakjlads""")
# escreve a frase inteira
print(frase.upper().count('O'))
#transoforma todas as letras da frase em maiusculas e em seguida faz a contagem

