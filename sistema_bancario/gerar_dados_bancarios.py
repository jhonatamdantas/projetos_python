import random

def gerar_agencia():
    return str(random.randint(1000, 9999))

def gerar_conta():
    numero = random.randint(100000, 999999)  # 6 dígitos
    dv = random.randint(0, 9)                # dígito verificador
    return f"{numero}-{dv}"