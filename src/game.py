import random

OPCOES = ["Pedra", "Papel", "Tesoura"]


def jogada_computador():
    return random.choice(OPCOES)


def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"

    if (
        (jogador == "Pedra" and computador == "Tesoura")
        or (jogador == "Papel" and computador == "Pedra")
        or (jogador == "Tesoura" and computador == "Papel")
    ):
        return "Você venceu!"

    return "Computador venceu!"
