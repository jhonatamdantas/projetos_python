from conta_bancarias import ContaCorrente, ContaPoupanca, Banco, validar_idade
import json; from pathlib import Path
from gerar_dados_bancarios import gerar_agencia, gerar_conta
from login import saque_log, carregar_dados, atualizar_saldo

while True:
    CAMINHO_ARQUIVO = Path(__file__).parent / "clientes.json"
    if not CAMINHO_ARQUIVO.exists():
        CAMINHO_ARQUIVO.write_text("", encoding="utf-8")

    with open(CAMINHO_ARQUIVO, "r") as arquivo:
        try:
            leitura_dados = json.load(arquivo)
        except json.JSONDecodeError:
            leitura_dados = {"clientes": []}
    print("="* 30) ; print("BEM VINDO AO BANCO PYTHON") ; print("="* 30)
    acesso = input ("""
O que deseja? 
[1] CADASTRO 
[2] SACAR
[3] DEPOSITAR:
[4] SAIR
""")
    if acesso == '1':
        try:
            conta_dic = {"CC": 1, "CP": 2}
            nome = input ("Seu nome: ").capitalize()
            idade = int (input("Idade: "))
            validador = validar_idade (idade)
            if not validador:
                print("Menor de Idade")
                break
            verificar_conta = int (input ("""
1 - [CC] / 2 - [CP]
-> """))
            if verificar_conta in conta_dic.values(): 
                saldo = input ("Deseja Adicionar saldo? ")
                if saldo in "Ss": valor_saldo = float(input("Digite seu saldo: "))
                elif saldo in "Nn": valor_saldo = 0
                else: print("Resposta inválida."); break

                agencia = gerar_agencia() ; conta = gerar_conta()
                if verificar_conta == conta_dic["CC"]: dados = ContaCorrente(nome, idade, agencia, conta, valor_saldo)
                elif verificar_conta == conta_dic["CP"]: dados = ContaPoupanca(nome, idade, agencia, conta, valor_saldo)
                
            else:
                print("Digite o tipo de conta válido...") ; continue

            print(repr(dados))
            print("-"*10,"SEUS DADOS ","-"*10)
            print("Nome: ", dados.nome) ; print("Idade: ", dados.idade)
            print("Agência: ", dados.agencia) ; print("Conta: ", dados.conta)
            print("Saldo Atual: R$", dados._saldo)
            print("-"*20)

            leitura_dados["clientes"].append(dados.to_dict())
            with open(CAMINHO_ARQUIVO, "w+", encoding="utf-8") as f:
                json.dump(leitura_dados, f, ensure_ascii=False, indent=2)
                print("Cadastro Armazenado na Base de Dados!")
        except Exception as erro: print("Ocorreu um erro de Cadastro: ", erro); break 

    elif acesso == '2' or acesso == '3':
        try:
            carregar_dados()
        except json.JSONDecodeError as json_error:
            print("Não existe clientes cadastrados", json_error) ; break
        dados = saque_log()
        if not dados:
            print("Cliente não cadastrado!") ; print()
            continue
        nome, idade, agencia, conta, saldo, tipo_conta = dados

        tipos = {
            "ContaCorrente":ContaCorrente,
            "ContaPoupanca":ContaPoupanca
        }

        conta_atual = tipos[tipo_conta](nome, idade, agencia, conta, saldo)
        try:
            print(f"\n=== {tipo_conta.replace('Conta', 'Conta ')} ===")
            print(f"Titular: {conta_atual.nome}")
            print(f"Saldo atual: R$ {conta_atual._saldo:.2f}")
            valor = float(input(f"Valor para {'sacar' if acesso == '2' else 'depositar'}: R$"))

            if valor <= 0:
                raise ValueError ("Valor igual / abaixo de zero")
            
            if acesso == '2': # SACAR
                novo_saldo = conta_atual.sacar(valor)
        
            else:  # DEPÓSITO
                novo_saldo = conta_atual.depositar(valor)
                mensagem = "Depósito realizado com sucesso!"
                print(mensagem)

            atualizar_saldo(nome, agencia, conta, novo_saldo)
          
            print(f"Saldo atual: R$ {novo_saldo:.2f}\n")
            
        except ValueError as e: print(f"Erro: {e}\n")
        except Exception as e: print(f"Operação falhou: {e}\n")
    elif acesso == "4": print("="*15, "Saindo do Sistema..." ,"="*15); break
    else: print("="*30, "Digite uma opção válida", "="*30); print() ; continue