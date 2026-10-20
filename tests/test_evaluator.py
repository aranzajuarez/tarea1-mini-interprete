"""Pruebas del evaluador: del AST a un numero."""

from mini_interprete.cli import interpretar


def test_suma():
    assert interpretar("3 + 4") == 7


def test_resta():
    assert interpretar("10 - 3") == 7


def test_multiplicacion():
    assert interpretar("6 * 7") == 42


def test_division():
    assert interpretar("10 / 2") == 5


def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11


def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14

import pytest
from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeSintaxis, ErrorDeEvaluacion


# 1. Casos Normales Adicionales
def test_evalua_multiples_operaciones_combinadas():
    assert interpretar("10 + 5 - 2") == 13


def test_evalua_expresion_con_subparentesis():
    assert interpretar("(10 + 2) * (8 / 4)") == 24.0


# 2. Casos Frontera 
def test_evalua_restas_encadenadas_asociatividad():
    assert interpretar("10 - 3 - 2") == 5


def test_evalua_divisiones_encadenadas_asociatividad():
    assert interpretar("12 / 4 / 2") == 1.5


def test_evalua_division_entre_cero():
    with pytest.raises(ErrorDeEvaluacion):
        interpretar("10 / 0")


# 3. Entradas Inválidas
def test_rechaza_menos_unario():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("-3")


def test_rechaza_parentesis_vacios():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("()")