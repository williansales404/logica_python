'''
cont = 0
while cont<100 : #neste exemplo o se usar True sem o break no final ficaria um loop infinito
    print(cont)           #Como pode ver a condição sera satisfeita enquando o cont não for maior que 100
    cont=cont+1
    if cont == 100:
        break
'''

########################################################
'''
"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
contador = 10

###

contador /= 5
print(contador)
'''

########################################################
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')"
"""
######################################################

'''
#Repetições
#while (enquanto)
#Executa uma ação enquanto uma condição for verdadeira
#Loop infinito -> Quando um código não tem fim

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')

'''
#######################################################