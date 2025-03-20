'''
#primeira solução
while True:

    numero1 = input('digite o primeiro valor: ')

    numero2 = input('digite o segundo numero: ')

    operador = input ('operadores permitidos +-*/')

    operadores_permitidos = '+-*/'

    elif operador == '+':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 + numero_float2
        print(f"{numero_float1}  +  {numero_float2}  =  {soma}")
    
    elif operador == '-':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 - numero_float2
        print(f"{numero_float1}  -  {numero_float2}  =  {soma}")
    
    elif operador == '*':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 * numero_float2
        print(f"{numero_float1}  *  {numero_float2}  =  {soma}")

    elif operador == '/':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 / numero_float2
        print(f"{numero_float1}  /  {numero_float2}  =  {soma:.2f}")
    
    
    
    sair = input('deseja [s]air').lower().startswith('s')

    if sair is True:
        break
'''



############################################################################
#segunda solução
while True:

    numero1 = input('digite o primeiro valor: ')

    numero2 = input('digite o segundo numero: ')

    operador = input ('operadores permitidos +-*/')

    operadores_permitidos = '+-*/'
    ###############################################
    numeros_validos = None

    #se try não converter os valor para float pula para axcept
    numero_float1 = 0
    numero_float2 = 0
    try:
       numero_float1 = float(numero1)
       numero_float2 = float(numero2)

       numeros_validos = True
    except:
        numeros_validos = None #a flag numeros validos continua None=vazio

    if numeros_validos is None:
        print('numeros invalidos')
        continue

    if operador not in operadores_permitidos: #verifica se entrada de opercador esta em operador_permitidos
        print('operadores não permitidos')
        continue

    if len(operador) > 1: #verifica se a entrada e somente de um operador
        print('digite um operador')
        continue
################################################################
    if operador == '+':
        soma = numero_float1 + numero_float2
        print(f"{numero_float1}  +  {numero_float2}  =  {soma}")
    
    elif operador == '-':
        soma = numero_float1 - numero_float2
        print(f"{numero_float1}  -  {numero_float2}  =  {soma}")
    
    elif operador == '*':
        soma = numero_float1 * numero_float2
        print(f"{numero_float1}  *  {numero_float2}  =  {soma}")

    elif operador == '/':
        soma = numero_float1 / numero_float2
        print(f"{numero_float1}  /  {numero_float2}  =  {soma:.2f}")

#######################################################################

    sair = input('deseja [s]air').lower().startswith('s')

    if sair is True:
        break


    