

try:
    numero = input('Digite um numero inteiro: ')
    numero_inteiro = int(numero)

    if (numero_inteiro % 2) == 0 :
        print('par')
    else:
        print('impar')

except(TypeError, ValueError):
    print('erro, digite um valor inteiro')


#solução professor
'''
entrada = input('Digite um número: ')
#########################################################
 if entrada.isdigit():
     entrada_int = int(entrada)
     par_impar = entrada_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {entrada_int} é {par_impar_texto}')
 else:
     print('Você não digitou um número inteiro')
#########################################################
try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')

'''

  