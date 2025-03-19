

tabuada = input('deseja a tabuda de que numero: ')
tabuada1 = int(tabuada)

part_2_tabuada = input('ate que numero deseja fazer: ')
part_2_tabuada1 = int(part_2_tabuada)


linha = 1

coluna = 1

while linha <=  tabuada1:

    while coluna <= part_2_tabuada1:
        soma = linha * coluna

        print(f"{linha} {'x'} {coluna} {'='} {soma}")

        coluna += 1
    
    print(10*'=')
    coluna = 1
    
    linha += 1

    '''
    #primeira solução

    
linha = 1

coluna = 1

while linha <=  10:

    while coluna <= 10:
        soma = linha * coluna

        print(f"{linha} {'x'} {coluna} {'='} {soma}")

        coluna += 1
    
    print(10*'=')
    coluna = 1
    
    linha += 1
    '''
    
    