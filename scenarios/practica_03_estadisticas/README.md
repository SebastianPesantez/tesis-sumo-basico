# Práctica 3 – Generación y análisis de estadísticas en SUMO

## Objetivo
El objetivo de esta práctica es generar, exportar y analizar estadísticas
de una simulación de tráfico vehicular en SUMO, a partir de una red urbana
real obtenida desde OpenStreetMap.

En esta práctica se pasa de la visualización básica del tráfico
a un análisis cuantitativo y visual de los resultados de la simulación.

---

## Escenario de simulación

La simulación se basa en:
- Una red urbana real (`red_osm.net.xml`)
- Rutas de tráfico generadas automáticamente (`rutas_osm.rou.xml`)
- Una duración total de simulación de 600 segundos

---

## Estructura del directorio
practica_03_estadisticas/
├── red_osm.net.xml
├── rutas_osm.rou.xml
├── simu_p3.sumocfg
├── tripinfo.xml
├── tripinfo.csv
├── fcd.xml
├── trajectories.xml
├── grafica_duracion.py
├── grafica_distancia_vs_duracion.py
├── duracion.png
├── dist_vs_duracion.png
└── trayectorias.png


---

## Archivo de configuración de la simulación

El archivo `simu_p3.sumocfg` define:
- La red vial utilizada
- Las rutas de los vehículos
- El tiempo de simulación
- Los archivos de salida estadísticos

Se habilitan explícitamente las siguientes salidas:
- Información por vehículo (`tripinfo`)
- Datos de posición y velocidad (`fcd`)
- Trayectorias completas (`trajectories`)

---

## Ejecución de la simulación

La simulación se ejecuta en modo batch utilizando SUMO:

```bash
sumo -c simu_p3.sumocfg


---

## Archivos de salida generados

### tripinfo.xml

Contiene información individual por vehículo, incluyendo:

- Duración del viaje
- Distancia recorrida
- Velocidad media
- Tiempo de espera
- Emisiones contaminantes

Este archivo constituye la principal fuente de datos para el análisis.

### tripinfo.csv

Archivo generado a partir de tripinfo.xml, utilizado para facilitar
el análisis de datos con Python u otras herramientas externas.

La conversión se realiza con el script oficial de SUMO:

python3 $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml -s , -o tripinfo.csv

### fcd.xml

Contiene información de posición y velocidad de cada vehículo
en cada instante de tiempo de la simulación.

Este archivo se utiliza principalmente para la visualización
de trayectorias.

### trajectories.xml

Archivo que almacena las trayectorias completas de los vehículos,
útil para análisis espacio-temporal del tráfico.

La visualización de trayectorias se genera a partir del archivo fcd.xml
utilizando la herramienta incluida en SUMO:

python3 $SUMO_HOME/tools/plot_trajectories.py \
    -t xy \
    -o trayectorias.png \
    fcd.xml

El archivo trayectorias.png permite observar de forma visual
la dinámica del tráfico sobre la red urbana.

---

## Extraer trayectoria de un solo vehículo desde fcd.xml

Usamos una herramienta de SUMO oficial.

Ejecuta:

python3 $SUMO_HOME/tools/plot_trajectories.py \
  -t xy \
  --filter-ids 0 \
  -o trayectoria_veh_0.png \
  fcd.xml
  
Para dos trayectorias:

python3 $SUMO_HOME/tools/plot_trajectories.py \
  -t xy \
  --filter-ids 0,7 \
  -o trayectorias_veh_0_7.png \
  fcd.xml

---

## Extraer la velocidad vs tiempo de dos vehiculos

Comparar velocidad de dos vehículos reales

python3 $SUMO_HOME/tools/plot_trajectories.py \
  -t ts \
  --filter-ids 0,7 \
  -o velocidad_vs_tiempo_veh_0_7.png \
  fcd.xml

  
  
