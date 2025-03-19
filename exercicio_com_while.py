
'''
#primeira solução
nome = 'willian sales'
tamanho_nome = len(nome)
###########################
print(nome[0])
print(tamanho_nome)
##########################
cont = 0
while cont <= tamanho_nome :
    
    print("*" + nome[cont] + "*")

    cont += 1
'''

##############################################
'''
#solulão do professor
#Iterando strings com while
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
'''
###############################################

#segunda solição
nome = 'willian sales'

#esta variavel vazia vai ser possivel acumular valor dentro dela
#atraves do while
novo_nome = ''

cont = 0

while cont < len(nome):

    letra = nome[cont]

    novo_nome = novo_nome +f'*{letra}'

    cont += 1

novo_nome = novo_nome + '*'

print(novo_nome)
##############################################





















