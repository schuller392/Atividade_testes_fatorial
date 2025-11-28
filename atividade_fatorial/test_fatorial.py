import pytest
from fatorial import fatorial


@pytest.mark.parametrize("n,esperado", [
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (4,24),
    (5,120),
    (8,40320)
])

def test_fatorial_casos_validos(n, esperado):
    assert fatorial(n) == esperado