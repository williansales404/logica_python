horas = input('digite o horario: ')
hora_do_dia = int(horas)

if hora_do_dia >= 00 and hora_do_dia <= 11 :
    print('bom dia')

elif hora_do_dia >= 12 and hora_do_dia <= 17 :
    print('boa tarde')

elif hora_do_dia >=18 and hora_do_dia <=23 :
    print('boa noite')


#solução do professor
'''
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
'''