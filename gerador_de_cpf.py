# SITE VALIDADOR DE CPF
# https://www.4devs.com.br/validador_cpf

import random 
cpf = []

for i in range(0, 9):
    cpf.append(random.randint(0, 9))
print("Valores Gerados")
print(cpf)

cpf_pt1 = ""
for valor in cpf:
    cpf_pt1 += str(valor)
    
print()
print(f"O cpf gerado sem dígito final: {cpf_pt1}")

print()
multiplicar = []
for pos, valor in enumerate(cpf_pt1):
    conta = (int(10-pos) * int(valor))
    # print((10-pos,valor, "=", conta))
    multiplicar.append(conta)

digito_1 = ((sum(multiplicar) * 10) % 11)

if digito_1 == 10:
    print(f"O valor gerado foi {digito_1} Pela LEI, o valor 10, passa a ser 0")
    digito_1 = "0"
else:
    pass 

digito_1 = str(digito_1)
print(f"O primeiro dígito foi {digito_1}")
# cpf_final = str(cpf_final)
cpf_pt1 += digito_1
# print(cpf_final)

cpf_pt2 = cpf_pt1
multiplicar.clear()

for pos, valor in enumerate(cpf_pt2):
    conta = (int(11-pos) * int(valor))
    # print(11-pos, valor)
    multiplicar.append(conta)

digito_2 = ((sum(multiplicar)* 10) % 11)
digito_2 = str(digito_2)
print(f"O segundo dígito foi {digito_2}")

if digito_2 == "10":
    print(f"O valor gerado foi {digito_2} Pela LEI, o valor 10, passa a ser 0")
    digito_2 = "0" 
    cpf_pt2 += digito_2
else:
    cpf_pt2 += digito_2

print()
print(f"CPF sem formatação: {cpf_pt2}")

cpf_final = cpf_pt2

print()
print("CPF Formatado.")


cpf_formatado_final = f"{cpf_final[0:3]}.{cpf_final[3:6]}.{cpf_final[6:9]}-{cpf_final[9:11]}"

print(cpf_formatado_final)

