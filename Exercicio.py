import random

def jogar_dado():
    return random.randint(1, 6)

def main():
    num_rodadas = int(input("Quantas rodadas você deseja jogar? "))

    num_jogadores = int(input("Quantos jogadores vão participar? "))

    # Lista de jogadores
    jogadores = []

   
    for i in range(1, num_jogadores + 1):
        nome_jogador = input(f"Digite o nome do jogador {i}: ")
        jogador = {"nome": nome_jogador, "resultados": []}
        jogadores.append(jogador)

    # Loop 
    for rodada in range(1, num_rodadas + 1):
        print(f"\nRodada {rodada}:")
        
        # Cada jogador joga o dado
        for jogador in jogadores:
            resultado_dado = jogar_dado()
            jogador["resultados"].append(resultado_dado)
            print(f"{jogador['nome']} jogou o dado e obteve {resultado_dado}")

    # Ordenar os jogadores(máximo tirado no dado)
    jogadores.sort(key=lambda x: max(x["resultados"]), reverse=True)

    # Resultado final
    print("\nResultado Final:")
    for jogador in jogadores:
        vitorias = jogador["resultados"].count(max(jogador["resultados"]))
        print(f"{jogador['nome']} obteve {vitorias} vitória(s)")

    # Verificar empate
    if len(jogadores) > 1 and max(jogadores[0]["resultados"]) == max(jogadores[1]["resultados"]):
        print("Houve um empate!")
    else:
        print(f"\nO grande campeão é {jogadores[0]['nome']}!")

if __name__ == "__main__":
    main()

   