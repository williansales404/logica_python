frase = 'aaaa ooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    #########################################################################################################
    #quando tiver espaço ' ' no index o if incrementa +1 e volta para o while assim ignorando o espaço
    if letra_atual == ' ': 
        i += 1
        continue

    #############################################################################################################################
    #a função 'count' ira contar quantas vezes a 'letra atual' apare na frase de forma automatica conservando seu valor.
    #a função cout quando passa por determinada letra ja conserva o seu valor de quantas vezes essa letra aparece automaticamnete
    #o valor muda quando passa para outra letra.
    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)