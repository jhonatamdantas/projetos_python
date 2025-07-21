# 🧠 Quiz Matemático Interativo em Python

<a href="perguntas_ex.py">Quiz Matemático.py</a>

Este projeto é um pequeno jogo de perguntas matemáticas feito em **Python** que roda diretamente no console.  
Ele tem como objetivo testar o conhecimento do usuário em operações básicas (`+`, `-`, `*`, `/`), oferecendo opções de múltipla escolha e pontuando conforme o desempenho.

---

## 🚀 Funcionalidades

- Gera **perguntas aleatórias** com operações matemáticas básicas;
- Apresenta **quatro opções de resposta**, sendo uma correta e três alternativas;
- Aceita **entrada do usuário** pelo **índice da opção** ou pelo **valor numérico**;
- Mostra feedback de acerto/erro em tempo real;
- Permite jogar quantas rodadas quiser;
- Mostra a **pontuação final** no fim da sessão.

---

## 🧩 Como funciona

1. Um operador (`+`, `-`, `*`, `/`) é escolhido aleatoriamente;
2. Dois números inteiros são gerados aleatoriamente;
3. O jogo calcula o resultado da operação e gera 3 alternativas incorretas;
4. O usuário escolhe uma das opções;
5. O jogo verifica a resposta e atualiza os pontos;
6. O usuário decide se deseja continuar jogando.

---

## 📌 Destaques Técnicos

- Uso de `random.sample()` e `random.shuffle()` para gerar opções únicas e embaralhadas;
- Cálculos com `f"{valor:.2f}"` para formatar números decimais (divisão);
- Tratamento de erros com `try/except` para entradas inválidas;
- Limpeza de tela com `os.system("cls")` (para Windows).


<details>
<summary><strong>

```python
import os 
import random

def operar_valor(a, b):
    if operador == "*":
        return a * b
    if operador == "/":
        return f"{a / b:.2f}"
    if operador == "+":
        return a + b
    if operador == "-":
        return a - b

lista_valores_total = list(range(-50, 150))
lista_valores_div = [round(random.uniform(-50.0, 150.0), 2) for _ in range(3)]
pontos = 0

while True:
    operador = random.choice("+-*/")
    
    if operador == "/":
        lista_valores = lista_valores_div
    else:
        lista_valores = lista_valores_total
    
    v1 = random.randint(1, 150)
    v2 = random.randint(1, 150)

    resposta_correta = operar_valor(v1, v2)

    if resposta_correta in lista_valores:
        lista_valores.pop(resposta_correta)

    opcao = random.sample(lista_valores, 3)
    opcao.append(resposta_correta)
    random.shuffle(opcao)

    perguntas = [
        {
            "Pergunta": f"Quanto é {v1} {operador} {v2}",
            "Opções": opcao,
            "Resposta": str(resposta_correta)
        }
    ]

    print(perguntas[0]["Pergunta"])

    for i, num in enumerate(perguntas[0]["Opções"]):
        print(f"{i}) {num}")
    print()

    resposta_usuario = input("Digite sua Resposta (Índice / Valor): ")

    try:
        if resposta_usuario == perguntas[0]["Resposta"]:
            print("Acertou ✅")
            pontos += 1
        elif opcao[int(resposta_usuario)] == resposta_correta:
            print("Acertou ✅")
            pontos += 1
        elif resposta_usuario in "0123":
            print(f"Errou ❌ A resposta correta era {perguntas[0]['Resposta']}")
    except:
        try:
            int(resposta_correta)
            if int(resposta_usuario) in opcao:
                print(f"Errou ❌ A resposta correta era {perguntas[0]['Resposta']}")
            elif int(resposta_usuario) not in opcao:
                print(f"Resposta Fora das Alternativas ❌ A resposta correta era {perguntas[0]['Resposta']}")
        except:
            if len(resposta_usuario) == 0:
                print("Resposta Vazia")
            elif resposta_correta:
                print('Resposta Inválida ❌')

    while True:
        escolha_us = input("Quer Continuar [S/N]: ").strip().lower()
        if escolha_us in ("s", "n"):
            break
        os.system("cls")
        print("Erro, tente novamente.")
    
    continuar = escolha_us
    if continuar == "s":
        os.system("cls")
        continue
    else:
        os.system("cls")
        break

print("=" * 20, "FIM DO PROGRAMA", "=" * 20)
if pontos == 1:
    print(f"VOCÊ SÓ FEZ {pontos} PONTO 🤨")
elif pontos > 1:
    print(f"VOCÊ FEZ {pontos} PONTOS! 👌")
else:
    print("VOCÊ NÃO ACERTOU NADA, BORA PRATICAR EIN 😬")
