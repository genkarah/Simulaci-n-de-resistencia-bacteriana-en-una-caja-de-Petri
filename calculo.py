import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm





# Parámetros de la caja de Petri

filas = 50
columnas = 50

poblacion_sensible = 900
poblacion_resistente = 100

semilla = 42

capacidad_maxima = filas * columnas

print("Capacidad máxima:", capacidad_maxima)
print("Población inicial:", poblacion_sensible + poblacion_resistente)
print("Espacios vacíos:", capacidad_maxima - poblacion_sensible - poblacion_resistente)




def crear_caja_petri(filas, columnas, Ns, Nr, semilla=None):

    capacidad = filas * columnas

    # Validar dimensiones
    if filas <= 0 or columnas <= 0:
        raise ValueError("Las dimensiones deben ser positivas.")

    # Validar poblaciones
    if Ns < 0 or Nr < 0:
        raise ValueError("Las poblaciones no pueden ser negativas.")

    if not isinstance(Ns, (int, np.integer)) or not isinstance(Nr, (int, np.integer)):
        raise ValueError("Las poblaciones deben ser números enteros.")

    if Ns + Nr > capacidad:
        raise ValueError("La población supera la capacidad de la matriz.")

    # Crear generador aleatorio
    rng = np.random.default_rng(semilla)

    # Crear una matriz vacía
    caja = np.zeros((filas, columnas), dtype=np.uint8)

    # Seleccionar posiciones únicas aleatoriamente
    posiciones = rng.choice(
        capacidad,
        size=Ns + Nr,
        replace=False
    )

    # Convertir la matriz en una vista unidimensional
    caja_plana = caja.ravel()

    # Colocar bacterias sensibles
    caja_plana[posiciones[:Ns]] = 1

    # Colocar bacterias resistentes
    caja_plana[posiciones[Ns:]] = 2

    return caja


caja = crear_caja_petri(
    filas=filas,
    columnas=columnas,
    Ns=poblacion_sensible,
    Nr=poblacion_resistente,
    semilla=semilla
)

print(caja)
print("Dimensiones:", caja.shape)
