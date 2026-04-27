import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("5/7") == 71
    assert convert("1/2") == 50
    assert convert("1/1") == 100


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("8/7")  # x > y

    with pytest.raises(ZeroDivisionError):
        convert("5/0")  # División por cero

    with pytest.raises(ValueError):
        convert("1.5/5")  # No es entero

    with pytest.raises(ValueError):
        convert("h/l")  # No es número

    with pytest.raises(ValueError):
        convert("-1/5")  # Numeros negativos


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
