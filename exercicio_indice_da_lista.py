#primeira solução e a segunda usando um print diferente
lista = ['maria', 'victor', 'sandra' ]
lista.append('willian')


cont = 0
for nome in lista:
    #print(f'{cont} ,{lista[cont]}')
    print(f'{cont} ,{nome}')
    cont +=  1

'''
#solução professor
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

'''