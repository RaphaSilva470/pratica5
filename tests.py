from passwordVal import is_strong_password

def test_valid_password():
    assert is_strong_password("Abcdef1!")

def test_short_password():
    assert not is_strong_password("A1b!")

def test_no_uppercase():
    assert not is_strong_password("abcdef1!")

def test_no_lowercase():
    assert not is_strong_password("ABCDEF1!")

def test_no_number():
    assert not is_strong_password("Abcdefgh!")

def test_no_special_character():
    assert not is_strong_password("Abcdefg1")
