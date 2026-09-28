# test/test_weeek4.py


def test_always_passes():
    assert 2 + 2 == 4  # testing math


def test_string_is_lowercase():
    name = "ism3232"
    assert name == name.lower()  # operation


def test_path_segments():
    path = "/home/user/documents/ism3232/Module02_zsh"
    parts = path.split("/")
    assert "ism3232" in parts
