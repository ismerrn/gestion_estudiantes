"""Programa principal --> coordinar gestión de estudiantes"""

# Importamos métodos de otros módulos
from estudiantes.gestion import añadir_estudiante, obtener_estudiantes
from estudiantes.calculos import calcular_media, calcular_aprobado
from utils.mensajes import mostrar_estudiante

# REGISTRO DE ESTUDIANTES
total = int(input("Nº de Estudiantes: "))

for estudiante in range(total):
    # Usuario introduce el nombre del estudiante
    nombre = input("Nombre del estudiante: ").strip()

    notas = []

    while True:
        # Usuario introduce las 3 notas de ese estudiante
        entrada = input(f"Notas de {nombre} (separadas por comas): ")

        # Formateamos las notas
        notas = [float(n.strip()) for n in entrada.split(",")]

        break

    añadir_estudiante(nombre, notas)

# MUESTRA DE LOS RESULTADOS
for estudiante in obtener_estudiantes():
    nombre = estudiante["nombre"]
    notas = estudiante["notas"]
    media = calcular_media(notas)
    estado = "Aprobado" if calcular_aprobado(media) else "Suspendido"
    mostrar_estudiante(nombre, notas, media, estado)