# 💰 Expense Tracker (Python)

Gestor de gastos personales por consola, hecho con Python y SQLite.
Permite registrar gastos, consultarlos y ver cuánto se gasta en cada categoría.

## ✨ Funcionalidades

- Registrar gastos con descripción, monto, categoría y fecha
- Validación de datos (no acepta montos negativos ni descripciones vacías)
- Listado de gastos del más reciente al más antiguo
- Resumen del total gastado por categoría
- Base de datos local con SQLite
- Pruebas automáticas con pytest

## 🛠️ Tecnologías

- Python 3.10+
- SQLite (módulo `sqlite3` de la biblioteca estándar)
- pytest

## 🚀 Cómo ejecutarlo

```bash
git clone https://github.com/juanpablosierra24/expense-tracker-python.git
cd expense-tracker-python
python -m src.main
```

No necesita instalar dependencias para usar el programa.

## 🧪 Cómo correr las pruebas

```bash
python -m pip install pytest
python -m pytest -v
```

## 📁 Estructura del proyecto

```
expense-tracker-python/
├── src/
│   ├── database.py   # Acceso a la base de datos
│   └── main.py       # Menú por consola
├── tests/
│   └── test_database.py
└── README.md
```

## 🗺️ Próximas mejoras

- [ ] Editar y eliminar gastos
- [ ] Filtrar por rango de fechas
- [ ] Exportar a CSV
- [ ] Presupuesto mensual por categoría

## 👤 Autor

**Juan Pablo Sierra**: [GitHub](https://github.com/juanpablosierra24)