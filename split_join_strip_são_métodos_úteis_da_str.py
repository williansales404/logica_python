"""
split e join com list e str

split - divide uma string em (list), vai pegar espaços em branco para 
dividir ou separa de acordo com o parametro desejado tranformando em lista.

join - une uma string, usado somente com valor iteraveis

strip - corta espaço, rstrip - corta espaço a direita, lstrip - corta espaço a esquerta.
"""

#metodo abaixo e so um exemplo de mudar valor mas não e recomendado muda o valor diretamente assim.
frase = '   Olha só que   , coisa interessante          '

lista_frase_crua = frase.split(', ')

lista_frase = []

for i, frase in enumerate(lista_frase_crua) :
    lista_frase.append(lista_frase_crua [i].strip())


#print(lista_frase_crua)
#print(lista_frase)

frases_unidas = ', '.join(lista_frase) # retorna a string corrigida

print(frases_unidas)

#####################################################################################################