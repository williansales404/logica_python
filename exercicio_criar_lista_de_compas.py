lista = []


while True:
    opcoes = str(input('[i]nserir [a]apagar [l]ista: '))
    opcoes_str = opcoes.lower()
        
    
    if len(opcoes_str) > 1:
        print('digite apenas um caracter')
        continue
#######################################################################################

    if opcoes_str == 'i':
        entrada = input('carinho de compra ')
        lista += entrada.split()
        print(lista)
        continue
########################################################################################

    if opcoes_str == 'a':

        try:
            indice = int(input('digite o indice do produto '))
            del lista [indice]

        except IndexError:
            print('erro indice não existe')
        except ValueError:
            print('erro digite um valor inteiro')
        continue
########################################################################################

    if opcoes_str == 'l':
        for N, lista_de_compra in enumerate(lista):
            print(f'indice: {N} produto: {lista_de_compra}')

        if lista == []:
            print('carinho de compra vazio')
        continue

    

########################################################################################
#########################SOLUÇÃO PROFESSOR##############################################
'''
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')

'''
########################################################################################