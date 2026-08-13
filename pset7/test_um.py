from um import count


def test_single_um():
    assert count("um") == 1


def test_case_insensitive():
    assert count("Um, thanks for the album.") == 1
    assert count("um... UM, uM") == 3


def test_no_um():
    assert count("yummy") == 0
    assert count("hello world") == 0
    assert count("") == 0
