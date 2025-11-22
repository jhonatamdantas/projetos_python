# from conta_bancarias import Conta, ContaCorrente, ContaPoupanca
from pathlib import Path; import json
CAMINHO_ARQUIVO = Path(__file__).parent / "clientes.json" 

def carregar_dados():
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def saque_log() -> bool:
    print("\n=== Verificando Dados ===")
    try:
        nome_log = input("Digite seu nome: ").strip().capitalize()
        agencia_log = input("Agência: ").strip()
        conta_log = input("Conta: ").strip()

        dados_login = carregar_dados()
        for usuario in dados_login['clientes']:
            if usuario['nome'] == nome_log and \
            usuario['agencia'] == agencia_log and \
            usuario ['conta'] == conta_log:
                print("Login feito com sucesso!")
                dados_us = usuario['nome'], usuario['idade'], usuario['agencia'], usuario ['conta'], usuario['saldo'], usuario['tipo_conta']
                return True and dados_us
                
    except (ValueError, TypeError) as erro:
        print(erro) 

def atualizar_saldo(nome, agencia, conta, novo_saldo, arquivo=CAMINHO_ARQUIVO):
    with open(CAMINHO_ARQUIVO, "r+", encoding="utf-8") as f:
        dados = json.load(f)

    for cliente in dados['clientes']:
        if cliente['nome'] == nome and cliente['agencia'] == agencia and cliente['conta'] == conta:
            cliente['saldo'] = round(float(novo_saldo), 2)
            break

    with open(CAMINHO_ARQUIVO, "w+", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)