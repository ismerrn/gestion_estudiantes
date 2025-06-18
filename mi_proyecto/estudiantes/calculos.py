"""Módulo de cálculos (notas + aprobado/suspenso)"""

def calcular_media(notas):

    if notas:
        return round(sum(notas) / len(notas), 2)
    return 0.0

def calcular_aprobado(media):
    return media >= 5.0