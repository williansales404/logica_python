nomebg = 'willian sales'
idadegb = '29'

nome = input('digite seu nome: ')

idade_entrada = input('digite sua idade: ')
idade = int(idade_entrada)


if nome == '' or idade_entrada == '':
    print('Desculpa voce deixo um campo vazio')
else:
    print(f'Seu nome e {nome}')
    tamanNome = len(nome)+1

    print('Seu nome invertido e '+nome[-1:-tamanNome:-1])

    if ' ' in nome:
        print('Seu nome contem espaço')
    else:
         print('Seu nome não contem espaço')

    tamanNome1 = len(nome)
    print(f'Seu nome tem {tamanNome1} letras')

    print('A primeira letra do seu nome e ' + nome[:1])

    print('Ultima letra do seu nome e ' + nome[-1:])

#Solução professor
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."

################################################################################
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

#Usando a expressão abaixo se a string estiver vazia da false.
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")

################################################################################
"""
