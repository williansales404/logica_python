
#####################################################################################
#minha soluçaõ para primeiro digito
'''
# comentario ou comentar no meu notebook e ctrl + ;
#80439153000
entrada_str = ''
indice = 0
valor = 10
soma = 0
calculo = 0
diisao = 0
digito = 0

entrada = input('Digite seu cpf')

for i in entrada:
    if valor != 2:

        entrada_str += i
        calculo = int(entrada_str[indice]) * valor
        soma += calculo
        indice += 1
        valor -= 1
        
soma_final = soma * 10
divisao = soma_final % 11
digito_valido = 0 if divisao > 9 else divisao
print(digito_valido)

'''
####################################################################################
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

#######################validação usuario########################################
'''
#solução professor
#verificação do primeiro digito


#cpf = '70459984144'
# import re
# import sys

# cpf = input('digite o cpf ')
# cpf = re.sub(

#     r'[^0-9]', '',
#     cpf
# )

# entrada_repetida = cpf == cpf[0] * len(cpf)
# if entrada_repetida:
#     print('cpf invalido repetição')
#     sys.exit()
'''
#cpf = '70459984144'

#####################################################################################
import random

# todo o codigo esta dentro de um for para gerar cpf aliatorio
for _ in range(10):

    digito_cpf1 = ''
    contador_regressivo1 = 10

    for i in range(9):
        digito_cpf1 += str(random.randint(0,9))

    resultado1 = 0
    for digito in digito_cpf1:
        resultado1 += int(digito) * contador_regressivo1
        contador_regressivo1 -= 1

    digito1 = (resultado1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0
    #####################################################################################
    """
    Calculo do segundo dígito do CPF
    CPF: 746.824.890-70
    Colete a soma dos 9 primeiros dígitos do CPF,
    MAIS O PRIMEIRO DIGITO,
    multiplicando cada um dos valores por uma
    contagem regressiva começando de 11

    Ex.:  746.824.890-70 (7468248907)
    11 10  9  8  7  6  5  4  3  2
    *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
    77 40 54 64 14 24 40 36  0 14

    Somar todos os resultados:
    77+40+54+64+14+24+40+36+0+14 = 363
    Multiplicar o resultado anterior por 10
    363 * 10 = 3630
    Obter o resto da divisão da conta anterior por 11
    3630 % 11 = 0
    Se o resultado anterior for maior que 9:
        resultado é 0
    contrário disso:
        resultado é o valor da conta

    O segundo dígito do CPF é 0
    """
    digito_cpf2 = digito_cpf1 + str(digito1)
    contador_regressivo2 = 11

    resultado2 = 0
    for digito in digito_cpf2:
        resultado2 += int(digito) * contador_regressivo2
        contador_regressivo2 -= 1

    digito2 = (resultado2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0
    ####################################################################################
    validação_cpf = f'{digito_cpf1}{digito1}{digito2}'

    print(validação_cpf)