nome = 'luiz otavio'
altura = 1.80
peso = 95
texto = str(peso)
imc = peso / (altura * altura)
#########################################
linha1 = f'{nome} tem {altura} de altura'

#formata quantidade de casas decimais
linha2 = f'pesa {peso}  quilos e seu imc e {imc:.2f}'


print(linha1)
print(linha2)
