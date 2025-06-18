"""Módulo mostrar info por pantalla (con formato)"""

# Mostramos por consola la información del estudiante
def mostrar_estudiante(nombre, notas, media, estado):
    print(f"Nombre: {nombre}")
    print(f"Notas: {notas}")
    print(f"Media: {media:.2f}")
    print(f"Estado: {estado}")
    print("-" * 40)

# Mostramos por consola una serie de estadísticas globales de los datos introducidos en forma de resumen final
def mostrar_resumen_global(num_total, num_aprobados, num_suspendidos, media_general):
    print("Resumen global:")
    print(f"Total de estudiantes: {num_total}")
    print(f"Aprobados: {num_aprobados} ({(num_aprobados / num_total * 100):.0f}%)")
    print(f"Suspendidos: {num_suspendidos} ({(num_suspendidos / num_total * 100):.0f}%)")
    print(f"Media general del grupo: {media_general:.2f}")