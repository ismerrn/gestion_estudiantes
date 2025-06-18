"""Módulo gestión de estudiantes --> registrar + acceder estudiantes"""

# Lista global de los estudiantes (+ su info)
datos_estudiantes = []

# F xa añadir el estudiante (+ info) a la lista
def añadir_estudiante(nombre, notas):
    estudiante = {"nombre": nombre, "notas": notas}
    datos_estudiantes.append(estudiante)

# F xa acceder a la lista de estudiantes
def obtener_estudiantes():
    return datos_estudiantes
