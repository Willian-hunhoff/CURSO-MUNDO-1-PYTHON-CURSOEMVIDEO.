cont = 1
while(cont ==1):
    cidade = str(input('escreva o nome da sua cidade: ')).strip()
    print(cidade[:5].capitalize() == 'Santo')
    #cidade = cidade.split()
    #cidade[0] = cidade[0].capitalize()
    #print('Santo' in cidade[0])
    cont = int(input('escreva 1 para recomeçar e 0 para sair '))
print('Adeus até a proxima! ')