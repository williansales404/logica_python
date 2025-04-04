import re

#cpf = '988.239.690-93'\
    # .replace('.','').replace('-','').replace(' ',)

cpf = '988.239.690-93'

cpf = re.sub(

r'[^0-9]', '',
cpf

)

entrada_repetida = cpf == cpf[0] * len(cpf)



print(entrada_repetida)
print(cpf)