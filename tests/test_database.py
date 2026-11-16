import pytest

from src.database import (
    init_db,
    agregar_gasto,
    listar_gastos,
    resumen_por_categoria,
)


@pytest.fixture
def db(tmp_path):
    """Base de datos temporal: no toca tu gastos.db real."""
    ruta = tmp_path / "test.db"
    init_db(ruta)
    return ruta


def test_agregar_y_listar_gasto(db):
    agregar_gasto("Almuerzo", 15000, "Comida", db_path=db)
    gastos = listar_gastos(db)
    assert len(gastos) == 1
    assert gastos[0]["descripcion"] == "Almuerzo"
    assert gastos[0]["monto"] == 15000
    assert gastos[0]["categoria"] == "comida"


def test_monto_cero_o_negativo_falla(db):
    with pytest.raises(ValueError):
        agregar_gasto("Error", 0, "otros", db_path=db)
    with pytest.raises(ValueError):
        agregar_gasto("Error", -500, "otros", db_path=db)


def test_descripcion_vacia_falla(db):
    with pytest.raises(ValueError):
        agregar_gasto("   ", 1000, "otros", db_path=db)


def test_lista_vacia_al_inicio(db):
    assert listar_gastos(db) == []


def test_resumen_por_categoria(db):
    agregar_gasto("Almuerzo", 15000, "comida", db_path=db)
    agregar_gasto("Cena", 20000, "comida", db_path=db)
    agregar_gasto("Bus", 3000, "transporte", db_path=db)
    resumen = {f["categoria"]: f["total"] for f in resumen_por_categoria(db)}
    assert resumen == {"comida": 35000, "transporte": 3000} 