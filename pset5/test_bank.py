from bank import value


def test_cero_case():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_20_case():
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("HEY") == 20


def test_hundred_case():
    assert value("que tal?") == 100
    assert value("como estas?") == 100
