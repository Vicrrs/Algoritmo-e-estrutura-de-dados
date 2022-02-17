from random import choice

jogador_vitorias = 0
mq_vitorias = 0



def Opcao_jogador():
    esc_jogador = str(input("Escolha Pedra, Papel ou Tesoura: "))
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opção Inválida! Tente Novamente")
        Opcao_jogador() #Para ler tudo novamente caso escolha algo inválido
    


def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"]) #choice escolhe uma das variaveis de dentro da lista
    return esc_maquina



while True:
    
    print("-=" * 15)
    esc_jogador = Opcao_jogador()
    esc_maquina = Opcao_Maquina()
    print("-=" * 15)
    
    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
            #Jogador ganha
            print(f"Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}. "
            "Resultado: Você ganhou") #Concatenação de String
            jogador_vitorias += 1
            
    elif esc_jogador == esc_maquina:
        #Empate
        print(f"Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}. "
            "Resultado: Empate") #Concatenação de String
    else:
        #Máquina ganha
        print(f"Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}. "
            "Resultado: Você PERDEU") #Concatenação de String
        mq_vitorias += 1
    
    
    
    print("-=" * 15)
    print(f"Vitórias do Jogador: {jogador_vitorias}")
    print(f"Vitórias da Máquina: {mq_vitorias}")
    print("-=" * 15)
    
    esc_jogador = str(input("Você quer jogar novamente? [S/N]")).strip().upper()[0]
    if esc_jogador == "N":
        break
print("Até mais")
