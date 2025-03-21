"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.

- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.

    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.

Faça a contagem de tentativas do seu
usuário.
"""

"""
#primeira solução
palavra_secreta = 'python'
palavra = ''
cont = 0
tentativas = 0
while True:

    letra = str (input('digite uma letra qualquer:'))
    
    if len(letra) > 1:
        print('digite somente um caracter por vez')

    if letra in palavra_secreta:
        palavra += letra
        cont += 1
        print (letra)

        if cont == len(palavra_secreta):
            print(palavra)
    else:
        print('erro tente novamente')
    
    tentativas +=1
    print(tentativas)
"""

    ######################################################################################


"""
#segunda solução

palavra_secreta = 'python'
acertos = ''
tentativas = 0

while True:

    letra_digitada = str (input('digite uma letra qualquer:'))

    tentativas +=1
    
    if len(letra_digitada) > 1:
        print('digite somente um caracter por vez')
        continue

    if letra_digitada in palavra_secreta:
        acertos += letra_digitada

    armazenar_acertos_e_erros = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in acertos:
            armazenar_acertos_e_erros += acertos
        else:
            armazenar_acertos_e_erros += '*'
            
    print(armazenar_acertos_e_erros)
    
    if armazenar_acertos_e_erros == palavra_secreta:
        print('VOCE GANHO A PALAVRA ERA ',palavra_secreta)
        print(armazenar_acertos_e_erros)

        #zerando o jogo
        acertos = ''
        tentativas = 0
"""

"""
#solução professor
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

"""


    

    
