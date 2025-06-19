# Solicita al usuario que ingrese 5 temperaturas.
# Guarda las temperaturas en una lista.
# Calcula el promedio y la temperatura máxima.
# Verifica si todas las temperaturas están entre 15°C y 30°C.
# Si alguna temperatura está fuera de 10°C–35°C, muestra una advertencia

temperatura = []
for i in range(5):
    temp = int(input("Ingresa la temperatura: "))
    temperatura.append(temp)

promedio = sum(temperatura)/len(temperatura)
t_max = max(temperatura)

check = True # Variable para establecer el rango dentro de la variable "check"
for t in temperatura:
    if t < 15 or t >30:
        check = False
        break

if temp >= 15 and temp <= 30: # Esto es solamente para saber el rango aceptable, si no está, muestra lo del else
    print("Está dentro del rango estable")
else:
    print("Promedio fuera del rango estable")

if not check:
    print("Advertencia, esta fuera del rango") # Si no está en el rango puesto en la variable check, muestra el print de la advertencia