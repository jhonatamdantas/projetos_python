# 🔐 Gerador de Senhas Aleatórias (Python)

Este projeto é um **gerador de senhas seguras**, feito em Python, ideal para criar senhas aleatórias e fortes utilizando letras, números e símbolos.  
Simples, direto e ótimo para aprendizado de manipulação de strings, entrada de usuário e geração aleatória.

---

## 🎯 Objetivo

O objetivo é fornecer uma ferramenta simples e rápida para gerar senhas fortes e aleatórias com o número de caracteres definido pelo usuário, combinando:

- Letras maiúsculas e minúsculas
- Dígitos numéricos (0–9)
- Caracteres especiais (`@#$%*!&...`)

---

## ⚙️ Como funciona

1. O script exibe um cabeçalho de boas-vindas no console.
2. Solicita ao usuário a **quantidade de caracteres** desejada para a senha.
3. Gera uma senha aleatória com o comprimento especificado, utilizando:
   - `string.ascii_letters` → letras A-Z (maiúsculas e minúsculas)
   - `string.digits` → números de 0 a 9
   - `string.punctuation` → símbolos especiais
4. Exibe a senha gerada no console.

---

## 📌 Exemplo de execução

```bash
=========================
GERADOR DE SENHAS
=========================
Digite a quantidade desejada: 12
Senha gerada: mN#4q@8Ld*Zp


import random
import string

print("="*25)
print("GERADOR DE SENHAS")
print("="*25)

# Entrada do usuário
escolha = int(input("Digite a quantidade desejada: "))

# Função geradora de senha
def gerador_senhas(lenght=escolha):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(caracteres) for _ in range(lenght))
    return password

# Exibe a senha gerada
print(gerador_senhas())
