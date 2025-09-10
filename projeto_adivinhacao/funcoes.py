def quebrar_linha():
    print()

def tratar_vazio(user):
    if len(user) == 0:
        return True

def verificar_tipoint(user):
    try:
        float(user)
        return True
    except:
        return False

def valor_proximo(valor_digt, valor_sorted):
    diferenca = abs(valor_digt - valor_sorted)
    if diferenca >= 30:
        print("➡️ Muito longe!")
    elif diferenca >= 15 and diferenca <= 29:
        print("➡️ Longe, tente melhor!")
    elif diferenca  >= 6 and diferenca <= 14:
        print("➡️ Tá chegando perto...")
    elif diferenca >= 2 and diferenca <= 5:
        print("Quase lá!")
    elif diferenca == 1:
        print("Tá colado!")





# fazer um def para cada opcao de sorteio 

# A resposta depende da diferenca:
# >= 30: muito longe
# 15–29: longe
# 6–14: perto
# 2–5: quase lá
# 1: colado
# 0: acertou