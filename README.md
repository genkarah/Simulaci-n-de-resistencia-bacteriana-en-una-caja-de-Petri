# Simulaci-n-de-resistencia-bacteriana-en-una-caja-de-Petri
El objetivo de este modelo es simular y visualizar la mutación y adaptación de antibiótico sobre la bacteria Streptococcus pyogenes (estreptococo del grupo A) en una caja de Petri. El propósito es visualizar la evolución de está bacteria dependiendo a como se administre el tratamiento sugerido.


## DATOS
PATRIC / BV-BRC (Bacterial Bioinformatics Resource Center)

## Variables de Entrada (Parámetros del Sistema)
Estas son las constantes biológicas y ambientales que se configuran al inicio de la simulación para calibrar el modelo con datos reales:

* `tasa_crecimiento` (\(\mu\)): Probabilidad de que una bacteria se duplique con éxito en un paso de tiempo (basado en la tasa de división de *E. coli* cada 20-30 min).
* `cmi_sensible` (\(CMI_s\)): Concentración Mínima Inhibitoria para la cepa salvaje. Umbral de antibiótico que causa la muerte de bacterias sensibles.
* `cmi_resistente` (\(CMI_r\)): Concentración Mínima Inhibitoria para la cepa mutante. Tolerancia significativamente más alta al fármaco.
* `tasa_mutacion` (\(\alpha\)): Probabilidad de que ocurra un error genético durante la replicación celular, transformando una bacteria descendiente en una cepa resistente.
* `coeficiente_difusion` (\(D\)): Velocidad y alcance con la que el antibiótico se expande desde el punto de aplicación hacia las celdas vecinas.

---

##  Variables de Estado (Dinámica Interna)
Valores que el programa calcula y actualiza constantemente en cada celda \((x, y)\) durante cada iteración o "turno":

* `estado_celda`: Identificador del ocupante actual de la coordenada.
    * `0`: Vacío / Espacio disponible.
    * `1`: Bacteria Sensible.
    * `2`: Bacteria Resistente.
* `concentracion_antibiotico`: Cantidad numérica de medicamento presente en esa celda específica en el tiempo \(t\), determinada por la distancia al foco de origen y las leyes de difusión.

---

## Variables de Salida (Métricas de Medición)
Son los resultados y datos recolectados al final de cada iteración para evaluar el comportamiento del fenómeno y generar los reportes gráficos:

* `poblacion_sensible_total` (\(N_s\)): Conteo acumulado de celdas con valor `1` en cada paso de tiempo. Muestra la curva de decrecimiento tras aplicar el antibiótico.
* `poblacion_resistente_total` (\(N_r\)): Conteo acumulado de celdas con valor `2` en cada paso de tiempo. Muestra la curva de crecimiento logístico de la nueva cepa dominante.
* `tiempo_de_conquista` (\(T_c\)): Número de turnos o ciclos que le toma a la cepa resistente colonizar por completo las zonas con alta concentración de fármaco.
* `radio_halo_inhibicion` (\(R_h\)): Distancia (en celdas) desde el centro de aplicación del antibiótico hasta la posición de la bacteria viva más cercana. Mide la efectividad temporal del tratamiento.
