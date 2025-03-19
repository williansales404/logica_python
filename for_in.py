'''
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
'''

#########################################################
'''
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')
'''
##########################################################

"""
#For + Range
#range -> range(start, stop, step)"


numeros = range(10, 0, -1)

#variavel numero recebe cada valor do range que o 'numeros' e conserva o valor
#para cada numero em numeros

for numero in numeros:
    print(numero)
"""
##########################################################

'''
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
'''

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')