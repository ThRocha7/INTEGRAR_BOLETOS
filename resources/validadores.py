def cod_barras(cod:str)->str:
    if len(cod) == 54:
        cod = cod.split('.')
        cod = ''.join(cod)
        cod = cod.split(' ')
        cod = ''.join(cod)
        print(cod)
        return cod
    elif len(cod) == 47:
        print('certo')
        return cod
