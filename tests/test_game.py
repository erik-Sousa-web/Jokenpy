import sys
import os

sys.path.append(os.path.abspath("src"))

from game import verificar_vencedor


def test_empate():
    assert verificar_vencedor("Pedra", "Pedra") == "Empate"


def test_pedra_ganha():
    assert verificar_vencedor("Pedra", "Tesoura") == "Você venceu!"


def test_papel_ganha():
    assert verificar_vencedor("Papel", "Pedra") == "Você venceu!"


def test_tesoura_ganha():
    assert verificar_vencedor("Tesoura", "Papel") == "Você venceu!"


def test_computador_ganha():
    assert verificar_vencedor("Pedra", "Papel") == "Computador venceu!"