"""Módulo de cálculos (notas + aprobado/suspenso)"""
# Importamos métodos de otros módulos
from estudiantes.gestion import obtener_estudiantes

# Calculamos la media del estudiante
def calcular_media(notas):

    if notas:
        return round(sum(notas) / len(notas), 2)
    return 0.0

# Calculamos si el estudiante ha aprobado (tiene que tener media mayor/igual a 5)
def calcular_aprobado(media):
    return media >= 5.0

# Calculamos resumen global
def calcular_resumen_global (num_total, num_aprobados, num_suspendidos, media_general):
    num_total = len(obtener_estudiantes)
    num_aprobados = 0
    suma_medias = 0.0

    for estudiante in obtener_estudiantes:
        media = calcular_media(estudiante["notas"])
        suma_medias += media
        if calcular_aprobado (media):
            num_aprobados += 1

    # Calculamos el nº total de estudiantes
    num_suspendidos = num_total - num_aprobados

    # Calculamos la media de todos los estudiantes
    media_general = suma_medias / num_total if num_total > 0 else 0.0

    return num_total, num_aprobados, num_suspendidos, media_general