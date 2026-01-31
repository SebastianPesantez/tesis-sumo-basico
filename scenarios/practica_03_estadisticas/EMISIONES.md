# Práctica 3 – Visualización de emisiones vehiculares (CO₂) en SUMO

## Objetivo
Generar y visualizar un mapa de color de las emisiones de CO₂ producidas por los
vehículos en cada tramo de la red vial, utilizando SUMO y sus herramientas
oficiales de visualización, como parte del análisis ambiental del tráfico.

---

## 1. Escenario de trabajo

Se trabaja sobre un escenario urbano generado a partir de OpenStreetMap, el cual
incluye:

- red_osm.net.xml (red vial)
- rutas_osm.rou.xml (rutas de los vehículos)
- simu_p3.sumocfg (archivo de configuración de SUMO)

---

## 2. Creación del archivo adicional para emisiones

Para medir las emisiones en cada carretera, se creó un archivo adicional del
tipo `edgeData`, el cual indica a SUMO que registre datos de emisiones durante
toda la simulación.

Archivo creado:

- input-additional-edgeData.xml

Este archivo define:
- El tipo de datos a medir: emisiones
- El período de medición (duración total de la simulación)
- El archivo de salida donde se guardarán los resultados

---

## 3. Inclusión del archivo adicional en la configuración de SUMO

El archivo `input-additional-edgeData.xml` se incluyó en el archivo
`simu_p3.sumocfg` mediante la etiqueta `<additional-files>` dentro de la sección
`<input>`.

Esto permite que SUMO cargue el archivo adicional al iniciar la simulación.

---

## 4. Ejecución de la simulación con emisiones

La simulación se ejecutó desde la terminal con el siguiente comando:

sumo -c simu_p3.sumocfg

Al finalizar la ejecución, SUMO generó el archivo de salida:

- edgeData-output-v2.xml

Este archivo contiene las emisiones de CO₂ agregadas por cada borde de la red.

---

## 5. Visualización del mapa de color de emisiones CO₂

Para visualizar las emisiones en la red vial se utilizó el script oficial de
SUMO `plot_net_dump.py`, ejecutado directamente desde consola.

Comando utilizado:

python3 $SUMO_HOME/tools/visualization/plot_net_dump.py \
  -v \
  -n red_osm.net.xml \
  --measures CO2_abs,CO2_abs \
  --xlabel "[m]" \
  --ylabel "[m]" \
  --default-width 0.2 \
  -i edgeData-output-v2.xml,edgeData-output-v2.xml \
  --min-color-value 0 \
  --max-color-value 2000000 \
  --min-width-value 0 \
  --max-width-value 1 \
  --colormap turbo \
  -o co2_color_map.png

---

## 6. Resultados obtenidos

Se generó el archivo:

- co2_color_map.png

Este archivo muestra la red vial coloreada según la cantidad de CO₂ emitida en
cada tramo, donde:

- Colores más intensos representan mayores emisiones
- Colores más suaves indican menor impacto ambiental

---

## 7. Análisis

El mapa de emisiones permite identificar visualmente los tramos de la red con
mayor impacto ambiental, los cuales suelen coincidir con zonas de alta densidad
vehicular o baja velocidad promedio.

Este análisis es fundamental para estudios de:
- Contaminación urbana
- Planeación de tráfico sostenible
- Evaluación de políticas de movilidad

---

## 8. Conclusión

Mediante el uso de archivos adicionales `edgeData` y herramientas de
visualización incluidas en SUMO, es posible analizar y representar gráficamente
las emisiones vehiculares sin necesidad de scripts personalizados, utilizando
únicamente comandos ejecutados desde la terminal.
