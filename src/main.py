from src.database import (
    init_db,
    agregar_gasto,
    listar_gastos,
    resumen_por_categoria,
    eliminar_gasto,
)


def pedir_monto():
    while True:
        try:
            monto = float(input("Monto: ").replace(",", "."))
            if monto > 0:
                return monto
            print("El monto debe ser mayor que cero.")
        except ValueError:
            print("Escribe un número válido.")


def opcion_agregar():
    descripcion = input("Descripción: ")
    monto = pedir_monto()
    categoria = input("Categoría (comida, transporte, ocio...): ")
    try:
        agregar_gasto(descripcion, monto, categoria)
        print("Gasto guardado.")
    except ValueError as error:
        print(f"No se pudo guardar: {error}")


def opcion_listar():
    gastos = listar_gastos()
    if not gastos:
        print("Todavía no hay gastos registrados.")
        return
    for g in gastos:
        print(f"{g['fecha']} | {g['categoria']:<12} | ${g['monto']:>10,.0f} | {g['descripcion']}")


def opcion_resumen():
    filas = resumen_por_categoria()
    if not filas:
        print("Todavía no hay gastos registrados.")
        return
    for f in filas:
        print(f"{f['categoria']:<12} ${f['total']:>10,.0f}")
    print(f"{'TOTAL':<12} ${sum(f['total'] for f in filas):>10,.0f}")


def main():
    init_db()
    opciones = {"1": opcion_agregar, "2": opcion_listar, "3": opcion_resumen}
    while True:
        print("\n=== Gestor de gastos ===")
        print("1. Agregar gasto")
        print("2. Ver gastos")
        print("3. Resumen por categoría")
        print("4. Salir")
        eleccion = input("Elige una opción: ").strip()
        if eleccion == "4":
            print("¡Hasta luego!")
            break
        accion = opciones.get(eleccion)
        if accion:
            accion()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()