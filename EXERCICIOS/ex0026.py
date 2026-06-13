cont = 1
while(cont == 1):
    frase = str(input('escreva uma frase do seu desejo: ')).strip().upper()
    print('a letra a aparece {} vezes em {}'.format(frase.count('A'), frase))
    print('a primeira letra a é a {} letra'.format(frase.find('A')+1))
    print('a ultima letra a aparece na posição {}' .format(frase.rfind('A')+1))
    
    cont = int(input('escreva 1 para continuar e 0 para sair '))