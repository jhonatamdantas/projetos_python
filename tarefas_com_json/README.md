# ✅ Gerenciador de Tarefas (Python)

Este projeto é um gerenciador de tarefas no terminal, desenvolvido em Python, que permite ao usuário adicionar, listar, desfazer, refazer e limpar tarefas de forma simples.
Os dados são armazenados em um arquivo JSON, garantindo que as tarefas fiquem salvas mesmo após fechar o programa.

## 🎯 Objetivo

O objetivo do código é gerenciar tarefas do dia a dia diretamente no terminal, utilizando comandos rápidos para organização e produtividade.

## ⚙️ Como funciona

Ao iniciar o programa, ele tenta carregar as tarefas salvas no arquivo arquivo.json.

O usuário pode digitar uma nova tarefa ou usar um dos comandos disponíveis:

listar → mostra todas as tarefas atuais;

desfazer → remove a última tarefa adicionada;

refazer → restaura a última tarefa desfeita (caso exista);

clear → limpa a tela do terminal;

sair → encerra o programa.

As tarefas são salvas automaticamente no arquivo arquivo.json após cada ação.


📎 Código-fonte principal


```python
<details>
<summary><strong>

```python
import json
from time import sleep
from copy import deepcopy
from os import system

def salvar_dados(json):
    lista_copia = deepcopy(json)
    return lista_copia

backup = []
while True:
    try:
        with open("arquivo.json", "r", encoding="utf8") as arquivo:
            dados = json.load(arquivo)
            print("TAREFAS")
            if not backup:
                backup = salvar_dados(dados)
            for tarefa in dados:
                print(tarefa)
    
    except FileNotFoundError:
        dados = []
    except json.JSONDecodeError:
        dados = []
    
    print()
    print(" --- COMANDO CLEAR PARA LIMPAR O TERMINAL ---")
    print("Comandos: listar, desfazer, refazer, sair")
    tarefa = input("Digite sua tarefa ou um comando: ").strip().lower()
    if tarefa == "sair":
        print("Você saiu do programa")
        sleep(1.25)
        system("cls")
        break

    with open("arquivo.json", "w", encoding="utf8") as arquivo:
        if tarefa == "listar":
            if len(dados) == 0:
                print("Nenhuma tarefa")
                continue
            for i, check in enumerate(dados):
                print(f"{i} - {check}")

        elif tarefa == "desfazer":
            if len(dados) == 0:
                print("Nada a desfazer")
                continue
            
            dados.remove(dados[-1])
            print("Tarefa Feita ✅")

        elif tarefa == "refazer":
            i = 0
            if len(backup) == 0 or len(dados) == len(backup):
                print("Nada a refazer")
            else:
                for item in backup:
                    try:
                        if item in dados[i]:
                            i += 1
                            continue
                    except IndexError:
                        dados.append(item)
        
        elif tarefa == "clear":
            system("cls")
        
        else:
            backup.append(tarefa)
            dados.append(tarefa)
   
        json.dump(dados, arquivo, ensure_ascii=False)
    print()
