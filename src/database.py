import sqlite3
from contextlib import closing
from datetime import date
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "gastos.db"


def get_connection(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path=DB_PATH):
    """Crea la tabla de gastos si todavía no existe."""
    with closing(get_connection(db_path)) as conn, conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion TEXT NOT NULL,
                monto REAL NOT NULL CHECK (monto > 0),
                categoria TEXT NOT NULL,
                fecha TEXT NOT NULL
            )
            """
        )


def agregar_gasto(descripcion, monto, categoria, fecha=None, db_path=DB_PATH):
    """Guarda un gasto y devuelve su id."""
    if not descripcion.strip():
        raise ValueError("La descripción no puede estar vacía.")
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que cero.")
    fecha = fecha or date.today().isoformat()

    with closing(get_connection(db_path)) as conn, conn:
        cursor = conn.execute(
            "INSERT INTO gastos (descripcion, monto, categoria, fecha) "
            "VALUES (?, ?, ?, ?)",
            (descripcion.strip(), monto, categoria.strip().lower(), fecha),
        )
        return cursor.lastrowid


def listar_gastos(db_path=DB_PATH):
    """Devuelve todos los gastos, del más reciente al más antiguo."""
    with closing(get_connection(db_path)) as conn:
        return conn.execute(
            "SELECT * FROM gastos ORDER BY fecha DESC, id DESC"
        ).fetchall()