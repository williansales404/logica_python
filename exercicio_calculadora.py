'''
#primeira solução
while True:

    numero1 = input('digite o primeiro valor: ')

    numero2 = input('digite o segundo numero: ')

    operador = input ('operadores permitidos +-*/')

    operadores_permitidos = '+-*/'

    if operador == '+':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 + numero_float2
        print(f"{numero_float1}  +  {numero_float2}  =  {soma}")
    
    if operador == '-':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 - numero_float2
        print(f"{numero_float1}  -  {numero_float2}  =  {soma}")
    
    if operador == '*':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 * numero_float2
        print(f"{numero_float1}  *  {numero_float2}  =  {soma}")

    if operador == '/':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 / numero_float2
        print(f"{numero_float1}  /  {numero_float2}  =  {soma:.2f}")
    
    
    
    sair = input('deseja [s]air').lower().startswith('s')

    if sair is True:
        break
'''

while True:

    numero1 = input('digite o primeiro valor: ')

    numero2 = input('digite o segundo numero: ')

    operador = input ('operadores permitidos +-*/')

    operadores_permitidos = '+-*/'



    try:
       pass 
    except:
        pass

    
    if operador == '+':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 + numero_float2
        print(f"{numero_float1}  +  {numero_float2}  =  {soma}")
    
    if operador == '-':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 - numero_float2
        print(f"{numero_float1}  -  {numero_float2}  =  {soma}")
    
    if operador == '*':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 * numero_float2
        print(f"{numero_float1}  *  {numero_float2}  =  {soma}")

    if operador == '/':
        numero_float1 = float(numero1)
        numero_float2 = float(numero2)
        soma = numero_float1 / numero_float2
        print(f"{numero_float1}  /  {numero_float2}  =  {soma:.2f}")
    
    
    
    sair = input('deseja [s]air').lower().startswith('s')

    if sair is True:
        break

