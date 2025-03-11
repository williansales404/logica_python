nome = input('digite seu nome ')

tamanho_nome = len(nome)

if tamanho_nome <= 4 :
    print('seu nome e curto')

elif tamanho_nome >= 5 and tamanho_nome <= 6 :
    print('seu nome e normal')

elif tamanho_nome > 6 :
    print('seu nome e muito grande')


#solução do professor
'''
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

'''
