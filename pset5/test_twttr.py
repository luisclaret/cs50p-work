from twttr import shorten


def main():
    test_twttr()


def test_twttr():
    assert shorten("hola") == "hl"
    assert shorten("tu como estas? ") == "t cm sts? "
    assert shorten("patineta") == "ptnt"
    assert shorten("HOLA") == "HL"
    assert shorten("Yo tengo 2 hijos") == "Y tng 2 hjs"


if __name__ == "__main__":
    main()
