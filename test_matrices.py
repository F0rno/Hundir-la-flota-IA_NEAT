import matrices

def test_prueba():
    tablero1 = matrices.genera_tablero(filas=3, columnas=3)
    assert len(tablero1) == 3
    assert len(tablero1[0]) == 3
    tablero1 = matrices.genera_tablero()
    assert len(tablero1) == 10
    assert len(tablero1[0]) == 10

