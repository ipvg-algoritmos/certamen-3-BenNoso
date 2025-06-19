# Crea una matriz 3x3 para guardar las notas.
# Calcula el promedio de cada estudiante (por fila) y de cada asignatura (por columna).
# Verifica si todos los estudiantes aprobaron (nota >= 4.0).
# Muestra una alerta si algún promedio individual es menor a 3.5.

notas = [[7.0, 2.2, 2.6],
        [6.0, 4.6, 5.8],
        [6.7, 2.6, 3.5]]

for file in range(3):
    suma = 0
    for col in range(3):
        