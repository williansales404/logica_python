

try:
    numero = input('Digite um numero inteiro: ')
    numero_inteiro = int(numero)

    if (numero_inteiro % 2) == 0 :
        print('par')
    else:
        print('impar')

except(TypeError, ValueError):
    print('erro, digite um valor inteiro')

  