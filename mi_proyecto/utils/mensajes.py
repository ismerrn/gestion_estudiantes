"""Módulo mostrar info por pantalla (con formato)"""

# Mostramos por consola la información del estudiante
def mostrar_estudiante(nombre, notas, media, estado):
    print(f"Nombre: {nombre}")
    print(f"Notas: {notas}")
    print(f"Media: {media:.2f}")
    print(f"Estado: {estado}")
    print("-" * 40)