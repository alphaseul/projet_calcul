import pytest

def calcul(x):
    return x + 5

def test_method():
    assert calcul(5) == 10