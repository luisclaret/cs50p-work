from plates import is_valid


def test_plates():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CS50") == True
    assert is_valid("AAA022") == False
    assert is_valid("2AA222") == False
    assert is_valid("A2") == False
    assert is_valid("A") == False
    assert is_valid("AAAA") == True
    assert is_valid("9999") == False
    assert is_valid("Hola, como estas?") == False
    assert is_valid("H#22") == False
    assert is_valid("#$%&") == False
    assert is_valid(".,..") == False
    assert is_valid("") == False
    assert is_valid("AA 22") == False
