import random
import string


print("="*25)
print("GERADOR DE SENHAS")
print("="*25)
escolha = int (input("Digite a quantidade desejada: "))

def gerador_senhas(lenght=escolha):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(caracteres) for _ in range(lenght))
    return password
print(gerador_senhas())