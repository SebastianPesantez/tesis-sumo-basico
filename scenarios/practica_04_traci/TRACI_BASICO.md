# Introducción básica a TraCI (SUMO)

## Objetivo de la práctica

El objetivo de esta práctica es introducir el uso de la interfaz **TraCI (Traffic Control Interface)** para la simulación de tráfico vehicular en SUMO, permitiendo controlar la ejecución de la simulación desde scripts en Python. Se busca comprender cómo TraCI toma el control del tiempo de simulación y cómo se establece la comunicación cliente/servidor entre Python y SUMO.

---

## Herramientas utilizadas

- SUMO
- TraCI (librería Python)
- Python 3
- Entorno virtual (`sumo-venv`)
- Red y rutas generadas previamente en prácticas anteriores

---

## Estructura utilizada

La práctica se desarrolló dentro del directorio:

scenarios/practica_04_traci/

Con un subdirectorio para los scripts:

scenarios/practica_04_traci/scripts/

Los archivos de configuración de la simulación (`.sumocfg`) corresponden a prácticas anteriores y fueron reutilizados mediante rutas relativas.

---

## Prueba 1: Ejecución de SUMO con TraCI hasta que finalicen los vehículos

### Script utilizado
- traci_run_sumo.py

### Descripción del proceso

En esta prueba se ejecutó una simulación de SUMO controlada completamente por TraCI.  
El script inicia SUMO como un servidor TraCI y avanza la simulación paso a paso hasta que todos los vehículos hayan llegado a su destino.

La condición de parada se basa en el número mínimo esperado de vehículos activos en la simulación, obtenido desde TraCI.

### Comportamiento observado

- TraCI controla el avance de la simulación.
- La simulación finaliza automáticamente cuando no quedan vehículos en la red.
- El tiempo final de simulación no depende estrictamente del valor definido en la etiqueta `<end>` del archivo `.sumocfg`.

Este enfoque es adecuado cuando se desea que la simulación termine de forma natural, una vez completados todos los viajes.

---

## Prueba 2: Ejecución de SUMO con TraCI usando un número fijo de pasos

### Script utilizado
- traci_run_step.py

### Descripción del proceso

En esta prueba la simulación fue controlada mediante un contador de pasos definido en el script Python.  
Cada llamada a TraCI avanza la simulación exactamente un paso y el bucle se ejecuta hasta alcanzar un número máximo de pasos predefinido.

En este enfoque, TraCI asume completamente el control del tiempo de simulación, independientemente de los parámetros definidos en el archivo `.sumocfg`.

### Comportamiento observado

- Cada paso de TraCI equivale aproximadamente a un segundo de simulación.
- El tiempo total simulado depende exclusivamente del número de pasos definidos.
- La simulación puede continuar aun cuando ya no existan vehículos en la red.

Este método es útil para experimentos controlados y simulaciones reproducibles.

---

## Comparación entre ambos enfoques

| Criterio | Finalización por vehículos | Finalización por pasos |
|--------|---------------------------|------------------------|
| Control del tiempo | Implícito | Explícito |
| Condición de parada | Vehículos restantes | Número de pasos |
| Reproducibilidad | Media | Alta |
| Uso recomendado | Simulación natural | Experimentos controlados |

---

## Conclusiones

TraCI permite desacoplar el control del tiempo de simulación de la configuración tradicional de SUMO, otorgando al usuario control total desde Python.

Ambos enfoques son válidos y su uso depende del objetivo del experimento.  
Esta práctica establece la base para implementar control dinámico de vehículos, semáforos y otros elementos de la red vehicular en simulaciones más avanzadas.
