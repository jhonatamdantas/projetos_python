from random import randint
from os import system
import os
from time import sleep, time
from funcoes import quebrar_linha, tratar_vazio, valor_proximo, verificar_tipoint
import json

caminho_json = os.path.join("projeto_adivinhacao/dados.json")
while True:
    inicio = time()
    jogador = (input ("Digite seu nome: ")).strip().capitalize()

    if tratar_vazio(jogador): print("Nome Vazio");  sleep(1.15); system("cls");continue
    elif verificar_tipoint(jogador): print("Você digitou um valor"); sleep(1.15); system("cls"); continue
    else:
        system("cls")
        sleep(0.50)


        with open(caminho_json, "r") as arquivo:
            try:
                jogador_json = json.load(arquivo)
                print("Carreguei")
            
            except json.decoder.JSONDecodeError:
                jogadores = []
            
            try:
                jogador_existente = next((x for x in jogador_json if x['nome'] == jogador), None)

                if jogador_existente:
                    print("Jogador já existe na lista!")
                    sleep(0.25)
                    print(f"O jogador {jogador_existente['nome']} tem {jogador_existente['vitorias']} vitorias")
                else:
                    print(f"O jogador {jogador} não existe na lista")
            
            except:              
                jogador_existente = None

        
        quebrar_linha()

        print("="*20)
        print("🎯 BEM VINDO AO JOGO DE ADIVINHAÇÃO 🎯")
        print("="*20)
        quebrar_linha()

        while True:
                vitorias_jogador = 0
                escolha = int (input (
"""Escolha o nível de dificuldade:
[1] Fácil [1 a 10]
[2] Médio [1 a 50]
[3] Díficil [1 a 100]

>>> """))
                if escolha > 3 or escolha < 1:
                    print("Escolha Inválida...")
                    sleep(0.75)
                    system("cls")
                    continue
                break

        if escolha == 1:
            valor_sorteado = randint(1, 10)
        elif escolha == 2:
            valor_sorteado = randint(1, 50)
        elif escolha == 3:
            valor_sorteado = randint(1, 100) 

        tentativas = 1

        print("Número Secreto Gerado! Tente advinhar")
        print("Você tem 7 tentativas")
        quebrar_linha()

        while tentativas < 8:
            if tentativas == 7:
                print("Você tem apenas uma tentativa")
            quebrar_linha()
            try:
                valor_usuario = int (input (f"Tentativa{tentativas}>>> "))
                if valor_usuario == valor_sorteado:
                    quebrar_linha()
                    print("✅ Acertou! O valor foi", valor_usuario)
                    vitorias_jogador += 1
                    break
                
                valor_proximo(valor_usuario, valor_sorteado)
                tentativas += 1
                continue
            except:
                print("Valor Inválido", TypeError)
                continue
            
        print("Tentativas Esgotadas, o valor sorteado foi", valor_sorteado) if tentativas == 8 and vitorias_jogador == 0 \
        else quebrar_linha()

    with open(caminho_json, "w") as arquivo:
        if not jogador_existente:
            try:
                jogador_json.append({"nome": jogador, "vitorias": vitorias_jogador})
                json.dump(jogador_json, arquivo, indent=3)
            except:
                jogadores.append({"nome": jogador, "vitorias": vitorias_jogador})
                json.dump(jogadores, arquivo, indent=3)            
            continue

        for j in jogador_json:
            if j['nome'] == jogador:
                if vitorias_jogador > 0:
                    j["vitorias"] += 1
                    break

        json.dump(jogador_json, arquivo, indent=3)


    while True:
        continuar = input ("Quer Jogar Novamente? [S/N]: ").strip().lower()
        if continuar == "s" or continuar == "n":
            break

    if continuar == "s": continue
    elif continuar == 'n': break

