# 🧾 Gerador de CPF Válido (Python)

Este projeto é um **gerador de CPF** (Cadastro de Pessoa Física) feito em Python, que cria números de CPF **válidos** de acordo com as regras de validação oficiais.  
Ele pode ser usado para **fins educacionais, testes de sistemas** e aprendizado de lógica de programação.

🔗 Links úteis
<br>
<a href="https://www.4devs.com.br/validador_cpf" target="_blank" rel="external">Validador de CPF - 4Devs</a>
<br>
<a href="https://www.youtube.com/watch?v=2UXMe8hARg4&t=39s" target="_blank" rel="external">Vídeo explicativo do código no YouTube</a>

---

## 🎯 Objetivo

O objetivo do código é simular a geração de um número de CPF do zero, **calculando os dois dígitos verificadores finais** com base nos 9 primeiros números, seguindo o algoritmo utilizado pela Receita Federal.

---

## ⚙️ Como funciona

1. **Geração aleatória de 9 números** (os primeiros 9 dígitos do CPF);
2. **Cálculo do primeiro dígito verificador**:
   - Multiplica os 9 dígitos por pesos de 10 a 2;
   - Soma os resultados;
   - Multiplica o total por 10 e tira o resto da divisão por 11;
   - Se o resultado for 10, o dígito é 0.
3. **Cálculo do segundo dígito verificador**:
   - Aplica a mesma lógica, agora com os 10 primeiros dígitos (já incluindo o primeiro dígito verificador);
   - Usa pesos de 11 a 2.
4. O CPF final é exibido:
   - **Sem formatação**: apenas os números;
   - **Com formatação**: `XXX.XXX.XXX-XX`.

---

## 📷 Exemplo de saída no terminal

Valores Gerados
[7, 2, 4, 5, 1, 6, 9, 3, 0]

O cpf gerado sem dígito final: 724516930

O primeiro dígito foi 1
<br>
O segundo dígito foi 7

CPF sem formatação: 72451693017

CPF Formatado.
724.516.930-17



---

## 📎 Código-fonte

```python
import random 
cpf = []

# Gera 9 números aleatórios
for i in range(0, 9):
    cpf.append(random.randint(0, 9))
print("Valores Gerados")
print(cpf)

# Transforma lista em string
cpf_pt1 = ""
for valor in cpf:
    cpf_pt1 += str(valor)
    
print()
print(f"O cpf gerado sem dígito final: {cpf_pt1}")

# Calcula primeiro dígito
multiplicar = []
for pos, valor in enumerate(cpf_pt1):
    conta = (int(10 - pos) * int(valor))
    multiplicar.append(conta)

digito_1 = ((sum(multiplicar) * 10) % 11)
if digito_1 == 10:
    print(f"O valor gerado foi {digito_1} Pela LEI, o valor 10, passa a ser 0")
    digito_1 = "0"
digito_1 = str(digito_1)
print(f"O primeiro dígito foi {digito_1}")
cpf_pt1 += digito_1

# Calcula segundo dígito
cpf_pt2 = cpf_pt1
multiplicar.clear()
for pos, valor in enumerate(cpf_pt2):
    conta = (int(11 - pos) * int(valor))
    multiplicar.append(conta)

digito_2 = ((sum(multiplicar) * 10) % 11)
digito_2 = str(digito_2)
print(f"O segundo dígito foi {digito_2}")

if digito_2 == "10":
    print(f"O valor gerado foi {digito_2} Pela LEI, o valor 10, passa a ser 0")
    digito_2 = "0" 
cpf_pt2 += digito_2

# Mostra CPF sem e com formatação
print()
print(f"CPF sem formatação: {cpf_pt2}")

cpf_final = cpf_pt2
print()
print("CPF Formatado.")
cpf_formatado_final = f"{cpf_final[0:3]}.{cpf_final[3:6]}.{cpf_final[6:9]}-{cpf_final[9:11]}"
print(cpf_formatado_final)

