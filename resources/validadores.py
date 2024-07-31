def formatar_cod_barras(cod:str)->str:
    if len(cod) == 54:
        cod = cod.split('.')
        cod = ''.join(cod)
        cod = cod.split(' ')
        cod = ''.join(cod)
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
        return cnpj
    elif len(cnpj) == 14:
        print('certo')
        return cnpj
    

def formatar_agencia(agencia:str)->str:
    if len(agencia) <= 4:
        if len(agencia) == 1:
            agencia = '000' + agencia
            return agencia
        elif len(agencia) == 2:
            agencia = '00' + agencia
            return agencia
        elif len(agencia) == 3:
            agencia = '0' + agencia
            return agencia
        else:
            return agencia
    else:
        print('agencia invalida')


def formatar_valor_oracle(valor:str)->str:
    valor= valor.split('.')
    valor = ''.join(valor)
    vir = valor.index(',')
    if valor[vir:] == ',00':
        separar = valor.split(',')
        valor = separar[0]
        return valor
    else:
        return valor


def validador_valor(valor_oracle:str,valor_pla:str)->bool:
    valor = formatar_valor_oracle(valor_oracle)
    if valor_pla == valor:
        return True
    else: 
        print('valores divergentes')
        return False
    
