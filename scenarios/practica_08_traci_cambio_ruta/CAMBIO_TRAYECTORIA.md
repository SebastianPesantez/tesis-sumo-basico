# Práctica 1.12  
## Simulación de tráfico vehicular TraCI/SUMO  
## Cambio de trayectoria de vehículos

---

## Objetivos

- Integrar la interfaz TraCI con SUMO.
- Simular una red vehicular sobre SUMO utilizando scripts en Python.
- Cambiar la trayectoria de los vehículos que circulan en el mapa en función de una lógica de congestión.

---

## Introducción

TraCI proporciona una interfaz dinámica que permite interactuar en tiempo real con la simulación de tráfico en SUMO. Una de sus funcionalidades más importantes es la posibilidad de modificar el comportamiento de los vehículos durante la simulación, incluyendo el cambio de trayectoria en función de condiciones específicas del tráfico.

En esta práctica se implementa una lógica de congestión basada en la velocidad de los vehículos. Cuando un vehículo circula por una calle específica y su velocidad cae por debajo de un umbral definido, se considera que existe congestión y el vehículo es redirigido hacia una ruta alternativa. Este enfoque permite simular estrategias básicas de gestión de tráfico urbano y evaluar posibles mejoras en la movilidad.

---

## Herramientas utilizadas

- SUMO
- TraCI
- Python 3
- NetEdit (para inspección de la red vial)
- CSV (registro de resultados)

---

## Metodología

### 1. Identificación de calles (edges)

Para identificar las calles del mapa y sus posibles conexiones se utilizó la herramienta **NetEdit**.  
Mediante el modo *Select*, se seleccionó la calle principal donde suele presentarse congestión y se verificaron manualmente las rutas alternativas disponibles observando las conexiones de la red.

En esta práctica se trabajó con:

- Calle con congestión: `567060342#1`
- Calle alternativa: `1053072563`

---

### 2. Lógica de congestión

La lógica implementada en la simulación fue la siguiente:

- Se monitorea la velocidad de cada vehículo en cada paso de simulación.
- Si un vehículo:
  - se encuentra en la calle `567060342#1`
  - y su velocidad es menor a **10 m/s**
- entonces se considera que existe congestión.
- El vehículo es redirigido hacia la calle alternativa `1053072563`.
- Cada vehículo solo puede ser redirigido una vez.

---

### 3. Ejecución de la simulación

La simulación se ejecutó utilizando TraCI desde Python, conectándose a un archivo de configuración de SUMO previamente utilizado en prácticas anteriores.

Durante la simulación se registraron los siguientes datos en un archivo CSV:

- Tiempo de simulación (s)
- ID del vehículo
- Velocidad (m/s)
- Calle actual (edge)
- Indicador de redirección (SI / NO)

---

## Resultados

Al ejecutar la simulación se obtuvieron los siguientes resultados:

- La lógica de congestión se activó correctamente.
- Se detectaron múltiples vehículos con velocidades por debajo del umbral definido.
- Un total de **59 vehículos** fueron redirigidos hacia la ruta alternativa.
- El archivo `datos_change_trayectoria.csv` se generó correctamente como evidencia del proceso.

Ejemplo de salida por consola:

- Vehículos redirigidos por congestión detectada.
- Confirmación del cierre correcto de la simulación TraCI.

---

## Análisis

Los resultados demuestran que TraCI permite modificar dinámicamente la trayectoria de los vehículos durante la simulación en función de condiciones del tráfico. La estrategia aplicada representa un escenario realista de gestión vial, donde los vehículos evitan zonas congestionadas y toman rutas alternativas para mejorar el flujo vehicular.

En esta práctica no se generaron gráficas, ya que el objetivo principal fue validar el cambio de trayectoria y no realizar un análisis estadístico de variables continuas. El archivo CSV generado es suficiente como respaldo experimental.

---

## Conclusiones

- TraCI permite una interacción avanzada con SUMO, incluyendo la modificación dinámica de rutas.
- El uso de umbrales de velocidad es una estrategia sencilla y efectiva para detectar congestión.
- La redirección de vehículos puede simular políticas de tráfico urbano orientadas a mejorar la movilidad.
- Esta práctica sienta las bases para estudios más avanzados de control y optimización del tráfico.

---
