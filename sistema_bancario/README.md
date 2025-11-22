# 🏦 Mini Sistema Bancário em Python

Este projeto é um **sistema bancário simples**, totalmente funcional no terminal, feito em Python.  
Ele permite criar clientes, gerar contas automaticamente, realizar **saques, depósitos, login**, verificar saldo e armazenar todos os dados em um arquivo JSON.

O sistema foi construído com foco em organização, separação de módulos e uso de POO (Programação Orientada a Objetos).

---

## 🎯 Objetivo

O objetivo deste sistema é simular as operações essenciais de um banco:

- Cadastro de clientes  
- Geração automática de agência e conta  
- Contas Corrente e Poupança  
- Depósitos  
- Saques  
- Validação de login  
- Armazenamento persistente de dados  

---

## ⚙️ Como funciona

### 🔐 Login
O cliente informa **nome**, **agência** e **conta**.  
Os dados são validados contra o arquivo `clientes.json`.

### 🧍 Cadastro de Cliente
O usuário informa:
- Nome  
- Idade  
- Tipo de conta (CC ou CP)  
- Saldo inicial (opcional)  

O sistema automaticamente:
- Valida idade (apenas ≥ 18 anos)  
- Gera agência  
- Gera conta com dígito verificador  
- Salva no banco de dados JSON  

### 🏧 Saque / Depósito
Após login, o cliente pode:
- Sacar  
- Depositar  

O saldo é atualizado no arquivo `clientes.json`.

### 💾 Armazenamento
Todos os clientes ficam registrados em:

```
clientes.json
```

---

## 📷 Exemplo de funcionamento

```
==============================
BEM VINDO AO BANCO PYTHON
==============================

O que deseja?
[1] CADASTRO
[2] SACAR
[3] DEPOSITAR
[4] SAIR
```

Cadastro:

```
Seu nome: Lucas
Idade: 23
1 - [CC] / 2 - [CP]
-> 1
Deseja Adicionar saldo? S
Digite seu saldo: 500
Lucas, Sua conta foi criada com Sucesso!
Você recebeu um saldo extra de R$ 200,00
```

Login + Saque:

```
=== Verificando Dados ===
Digite seu nome: Lucas
Agência: 3922
Conta: 646867-2
Login feito com sucesso!

=== Conta Corrente ===
Titular: Lucas
Saldo atual: R$ 700.00
Valor para sacar: R$200
Saque realizado com sucesso
Saldo atual: R$ 500.00
```

---

## 📁 Estrutura do Projeto

- `main.py`  
- `conta_bancarias.py`  
- `gerar_dados_bancarios.py`  
- `login.py`  
- `clientes.json`  

---

## 🛠️ Tecnologias utilizadas

- Python 3  
- Programação Orientada a Objetos  
- JSON para banco de dados  
- `random` para geração de contas  
