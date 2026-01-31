# Práctica 3 – Análisis de densidad vehicular en SUMO

## Objetivo
Calcular y visualizar la densidad vehicular (#veh/km) en cada tramo de la red
vial utilizando SUMO y sus herramientas oficiales de visualización, como parte
del análisis estadístico de la simulación de tráfico.

---

## 1. Escenario de trabajo

Se utiliza un escenario generado a partir de OpenStreetMap, compuesto por los
siguientes archivos:

- red_osm.net.xml (red vial)
- rutas_osm.rou.xml (rutas vehiculares)
- simu_p3.sumocfg (configuración de la simulación)

---

## 2. Configuración de salidas para análisis de densidad

Para que SUMO calcule la densidad vehicular, se añadió la siguiente salida en el
archivo `simu_p3.sumocfg`, dentro de la sección `<output>`:

- edgedata-output → genera el archivo `edgedata.xml`

Este archivo contiene métricas agregadas por borde de la red, incluyendo la
densidad vehicular expresada en vehículos por kilómetro.

---

## 3. Ejecución de la simulación

La simulación se ejecuta desde la terminal utilizando el archivo de
configuración:

sumo -c simu_p3.sumocfg

Al finalizar la simulación, se generan los archivos de salida, incluyendo:

- edgedata.xml
- tripinfo.xml
- fcd.xml
- trajectories.xml

---

## 4. Verificación de la salida de densidad

Se comprueba la correcta generación del archivo de densidad mediante:

ls edgedata.xml

El archivo contiene información de densidad por cada borde de la red vial,
confirmando que SUMO calculó correctamente la métrica.

---

## 5. Visualización de la densidad vehicular

Para visualizar la densidad vehicular sobre la red vial se utiliza el script
oficial de SUMO `plot_net_dump.py`, ejecutado directamente desde consola.

El comando utilizado fue:

python3 $SUMO_HOME/tools/visualization/plot_net_dump.py \
  -v \
  -n red_osm.net.xml \
  --measures density,density \
  --xlabel "[m]" \
  --ylabel "[m]" \
  --default-width 0.5 \
  -i edgedata.xml,edgedata.xml \
  --min-color-value 0 \
  --max-color-value 5 \
  --min-width-value 0.5 \
  --max-width-value 3 \
  --colormap winter \
  -o density_color_map.png

Este comando genera una imagen donde:

- El color de cada tramo representa la densidad vehicular
- El ancho del tramo también varía según la densidad
- Los valores se expresan en #veh/km

---

## 6. Resultado obtenido

Se genera el archivo:

- density_color_map.png

Este archivo muestra la red vial coloreada según la densidad vehicular,
permitiendo identificar visualmente:

- Zonas de alta congestión
- Tramos con baja densidad
- Distribución espacial del tráfico

---

## 7. Conclusión

El análisis de densidad vehicular permite evaluar el nivel de congestión de la
red de tráfico de forma visual y cuantitativa. Mediante el uso del archivo
`edgedata.xml` y herramientas oficiales de SUMO ejecutadas desde consola, se
obtiene una representación clara del comportamiento del tráfico en la red.

Este análisis constituye una base fundamental para estudios posteriores como:
- Comparación densidad–velocidad
- Identificación de cuellos de botella
- Evaluación de estrategias de control de tráfico
