"""
 Formatação básica de strings
 s - string
 d - int
 f - float
 .<número de dígitos>f
 x ou X - Hexadecimal
 (Caractere)(><^)(quantidade)
 > - Esquerda
 < - Direita
 ^ - Centro
 = - Força o número a aparecer antes dos zeros
 Sinal - + ou -
 Ex.: 0>-100,.1f
 Conversion flags - !r !s !a 

 nome = "João"
idade = 30
mensagem = f"Meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)
# Saída: Meu nome é João e eu tenho 30 anos.

frase = "Olá, mundo!"
tamanho = len(frase)
print(f"A frase tem {tamanho} caracteres.")
# Saída: A frase tem 11 caracteres.

numeros = [1, 2, 3, 4, 5]
tamanho = len(numeros)
print(f"A lista tem {tamanho} elementos.")
# Saída: A lista tem 5 elementos.

dados = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
tamanho = len(dados)
print(f"O dicionário tem {tamanho} pares de chave-valor.")
# Saída: O dicionário tem 3 pares de chave-valor.

 """
 
variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
