from lanzar_escucha_ip import *

def test_laun():

    assert lanzarIP() == (True, str) or lanzarIP() == (False, str)

def test_escuchar():
    assert escuchar() == (True, str) or escuchar() == (False, str)