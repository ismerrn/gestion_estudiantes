"""Programa principal --> coordinar gestión de estudiantes"""

# Importamos métodos de otros módulos
from estudiantes.gestion import añadir_estudiante, obtener_estudiantes
from estudiantes.calculos import calcular_media, calcular_aprobado
from utils.mensajes import mostrar_estudiante

# Incluimos datos
añadir_estudiante("Juan", [7.0, 8.5, 6.0])
añadir_estudiante("Lucía", [5.0, 4.5, 6.0])
añadir_estudiante("Mario", [9.0, 9.5, 10.0])

# Mostramos los resultados
for estudiante in obtener_estudiantes():
    nombre = estudiante["nombre"]
    notas = estudiante["notas"]
    media = calcular_media(notas)
    estado = "Aprobado" if calcular_aprobado(media) else "Suspendido"
    mostrar_estudiante(nombre, notas, media, estado)