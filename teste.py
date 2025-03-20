# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.
# print(11) # int
# print(-11) # int
# print(0)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
# print(1.1, 10.11)
# print(0.0, -1.5)

# A função type mostra o tipo que o Python
# inferiu ao valor.
#print(type('Otávio'))
#print(type(0))
#print(type(1.1), type(-1.1), type(0.0))


# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
#conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
#print(conta_1)

'''
nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))'
'''
'''
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print('Olha meu print aqui')
'''

#if 1 and 1:
#    print(True and 1 and False)

'''
senha = input("digite a senha ")
busca = input('O QUE DESEJA BUSCA')

if busca in senha:
    print(f'sua senha {senha} tem {busca}')
else:
    print(f'sua senha {senha} não tem {busca}')'
'''

'''
nome = 'willian'
tamanNome = len(nome)+1
print(nome[-1:-tamanNome:-1])
print("tem " + nome[-1:])
'''
start = 0
end = 10
while start < end:
    start += 1
    print(start)




