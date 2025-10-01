# inventario.py
# Proyecto de gestión simple de inventario y ventas
# Compatible con Python 3
# Autor: Rodrigo Uriarte (para GitHub)
# --------------------------------------------

import datetime
import random

# ------------------------------
# Datos simulados de inventario
# ------------------------------
productos = [
    {"id": 1, "nombre": "Laptop", "stock": 10, "fecha_ingreso": datetime.date(2025, 6, 1)},
        {"id": 2, "nombre": "Mouse", "stock": 50, "fecha_ingreso": datetime.date(2025, 8, 15)},
            {"id": 3, "nombre": "Teclado", "stock": 30, "fecha_ingreso": datetime.date(2025, 7, 20)},
                {"id": 4, "nombre": "Monitor", "stock": 5, "fecha_ingreso": datetime.date(2025, 5, 10)},
                ]

                ventas = []  # lista para guardar ventas

                # ------------------------------
                # Ejercicio 1: días en inventario
                # ------------------------------
                def dias_en_inventario():
                    hoy = datetime.date.today()
                        for p in productos:
                                dias = (hoy - p["fecha_ingreso"]).days
                                        print(f"Producto: {p['nombre']} | Stock: {p['stock']} | Días en inventario: {dias}")

                                        # ------------------------------
                                        # Ejercicio 2: simular ventas
                                        # ------------------------------
                                        def simular_ventas():
                                            hoy = datetime.date.today()
                                                for _ in range(15):  # 15 ventas aleatorias
                                                        producto = random.choice(productos)
                                                                fecha_venta = hoy - datetime.timedelta(days=random.randint(0, 40))
                                                                        cantidad = random.randint(1, 3)

                                                                                if producto["stock"] >= cantidad:
                                                                                            producto["stock"] -= cantidad
                                                                                                        ventas.append({"producto": producto["nombre"], "cantidad": cantidad, "fecha": fecha_venta})

                                                                                                            # Ventas de los últimos 30 días
                                                                                                                ultimos_30 = [v for v in ventas if (hoy - v["fecha"]).days <= 30]
                                                                                                                    print("\nVentas en los últimos 30 días:")
                                                                                                                        for v in ultimos_30:
                                                                                                                                print(v)

                                                                                                                                # ------------------------------
                                                                                                                                # Ejercicio 3: bajo stock y +90 días
                                                                                                                                # ------------------------------
                                                                                                                                def analizar_inventario():
                                                                                                                                    hoy = datetime.date.today()
                                                                                                                                        print("\nProductos con bajo stock (<10):")
                                                                                                                                            for p in productos:
                                                                                                                                                    if p["stock"] < 10:
                                                                                                                                                                print(f"- {p['nombre']} | Stock: {p['stock']}")

                                                                                                                                                                    print("\nProductos con más de 90 días en inventario:")
                                                                                                                                                                        for p in productos:
                                                                                                                                                                                dias = (hoy - p["fecha_ingreso"]).days
                                                                                                                                                                                        if dias > 90:
                                                                                                                                                                                                    print(f"- {p['nombre']} | {dias} días en inventario")

                                                                                                                                                                                                    # ------------------------------
                                                                                                                                                                                                    # Ejercicio 4: salarios
                                                                                                                                                                                                    # ------------------------------
                                                                                                                                                                                                    empleados = [
                                                                                                                                                                                                        {"nombre": "Ana", "salario_base": 1000, "antiguedad": 5},
                                                                                                                                                                                                            {"nombre": "Luis", "salario_base": 1200, "antiguedad": 2},
                                                                                                                                                                                                                {"nombre": "Sofía", "salario_base": 900, "antiguedad": 8},
                                                                                                                                                                                                                ]

                                                                                                                                                                                                                def calcular_salarios():
                                                                                                                                                                                                                    print("\nSalarios calculados:")
                                                                                                                                                                                                                        hoy = datetime.date.today()
                                                                                                                                                                                                                            for e in empleados:
                                                                                                                                                                                                                                    antiguedad_bonus = e["antiguedad"] * 50
                                                                                                                                                                                                                                            dias_ultima_venta = None

                                                                                                                                                                                                                                                    if ventas:
                                                                                                                                                                                                                                                                ultima_venta = max(ventas, key=lambda v: v["fecha"])
                                                                                                                                                                                                                                                                            dias_ultima_venta = (hoy - ultima_venta["fecha"]).days

                                                                                                                                                                                                                                                                                    salario_total = e["salario_base"] + antiguedad_bonus
                                                                                                                                                                                                                                                                                            print(f"{e['nombre']} | Salario: {salario_total} | Días desde última venta: {dias_ultima_venta}")

                                                                                                                                                                                                                                                                                            # ------------------------------
                                                                                                                                                                                                                                                                                            # Ejercicio 5: reportes
                                                                                                                                                                                                                                                                                            # ------------------------------
                                                                                                                                                                                                                                                                                            def generar_reporte():
                                                                                                                                                                                                                                                                                                print("\n--- REPORTE GENERAL ---")
                                                                                                                                                                                                                                                                                                    timestamp = datetime.datetime.now()
                                                                                                                                                                                                                                                                                                        print(f"Generado el: {timestamp}\n")

                                                                                                                                                                                                                                                                                                            for p in productos:
                                                                                                                                                                                                                                                                                                                    dias = (datetime.date.today() - p["fecha_ingreso"]).days
                                                                                                                                                                                                                                                                                                                            print(f"Producto: {p['nombre']} | Stock: {p['stock']} | Antigüedad: {dias} días")

                                                                                                                                                                                                                                                                                                                            # ------------------------------
                                                                                                                                                                                                                                                                                                                            # MAIN
                                                                                                                                                                                                                                                                                                                            # ------------------------------
                                                                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                dias_en_inventario()
                                                                                                                                                                                                                                                                                                                                    simular_ventas()
                                                                                                                                                                                                                                                                                                                                        analizar_inventario()
                                                                                                                                                                                                                                                                                                                                            calcular_salarios()
                                                                                                                                                                                                                                                                                                                                                generar_reporte()