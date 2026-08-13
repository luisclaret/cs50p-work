from numb3rs import validate

def test_outrange():
    assert validate("300.300.300.300") == False
    assert validate("256.0.120.2") == False
    assert validate("256.0.120.2") == False
    assert validate("120.300.120.2") == False

def test_string():
    assert validate("hola") == False
    assert validate("120.r.5.0.1") == False

def test_badseparation():
    assert validate("120,30,50,0") == False

def test_empty():
    assert validate("") == False
    assert validate("120") == False

def test_notenought():
    assert validate("120.20.0.") == False

def test_valid():
    assert validate("120.20.1.0") == True
    assert validate("0.0.0.0") == True

def test_wrongnumbers():
    assert validate("001.000.002.027") == False

def test_negative():
    assert validate("-2.20.30.55") == False
    
def too_many_bytes():
    assert validate("20.20.20.20.20") == False
