def formatar_cod_barras(cod:str)->str:
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


def formatar_cnpj(cnpj:str)->str:
    if len(cnpj) == 18:
        cnpj = cnpj.split('.')
        cnpj = ''.join(cnpj)
        cnpj = cnpj.split('/')
        cnpj = ''.join(cnpj)
        cnpj = cnpj.split('-')
        cnpj = ''.join(cnpj)
        print(cnpj)
        return cnpj
    elif len(cnpj) == 14:
        print('certo')
        return cnpj


def validador_valor(valor_oracle:str,valor_pla:str)->bool:
    if valor_pla == valor_oracle:
        return True
    else: 
        print('valores divergentes')
        return False