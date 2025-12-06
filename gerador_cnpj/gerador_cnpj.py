# GERAR CNPJ VÁLIDO
from random import randint
def calcular_digitos(cnpj, pesos):
    soma = 0

    for i, valor in enumerate(cnpj):
        soma += int(valor) * int(pesos[i])

    resto_divisao = soma % 11
    if resto_divisao < 2: 
        digito = 0
    else:
        digito = 11 - resto_divisao

    return str(digito)


def gerar_digitos(cnpj_final: str):
    pesos_digito_um = "543298765432"
    pesos_digito_dois = "6543298765432"
    digito_um = calcular_digitos (cnpj_final, pesos_digito_um)
    cnpj_final += digito_um     
    
    digito_dois = calcular_digitos(cnpj_final, pesos_digito_dois)
    cnpj_final += digito_dois
    return cnpj_final 

def cnpj_formatacao():
    cnpj = ""
    while len(str(cnpj)) < 8:
        cnpj = randint(00000000, 99999999)
    sufixo_cnpj = "000" + str(randint(1, 3))
    cnpj_com_sufixo = str(cnpj) + sufixo_cnpj
    cnpj_formado = gerar_digitos(cnpj_com_sufixo)

    cnpj_final = f'{cnpj_formado[0:2]}.{cnpj_formado[2:5]}.{cnpj_formado[5:8]}/{cnpj_formado[8:12]}-{cnpj_formado[12:15]}'

    return cnpj_final

print(cnpj_formatacao())