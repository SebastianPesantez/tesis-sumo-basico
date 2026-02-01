PRACTICA 1.11
SIMULACION DE TRAFICO VEHICULAR – TRACI / SUMO
CALCULO DE EMISIONES DE CO2


OBJETIVOS

- Integrar la interfaz TraCI con SUMO.
- Simular una red vehicular sobre SUMO utilizando scripts en Python.
- Calcular las emisiones de CO2 de los vehículos que circularon en el mapa.


INTRODUCCION

SUMO es una herramienta de simulación de tráfico que permite analizar el
comportamiento de vehículos en entornos urbanos. TraCI (Traffic Control
Interface) permite interactuar con la simulación en tiempo real, obteniendo
información detallada de los vehículos, como velocidad, posición y emisiones.

En esta práctica se utiliza TraCI para calcular y registrar las emisiones de
dióxido de carbono (CO2) producidas por los vehículos durante la simulación,
permitiendo evaluar el impacto ambiental del tráfico urbano.


HERRAMIENTAS UTILIZADAS

- SUMO
- TraCI
- Python 3

Librerías:
- traci
- csv
- pandas
- matplotlib
- seaborn
- scipy.stats


ESTRUCTURA DEL DIRECTORIO

practica_07_traci_co2/
│
├── scripts/
│   └── traci_co2.py
│
└── resultados/
    ├── datos_simulacion_co2.csv
    ├── co2_promedio_por_vehiculo.png
    └── co2_promedio_general.png


PROCEDIMIENTO

1. Se inicia la comunicación entre SUMO y TraCI desde un script en Python,
   indicando el archivo de configuración .sumocfg de la simulación.

2. Durante cada paso de la simulación se obtienen:
   - El tiempo de simulación en segundos.
   - Los identificadores de los vehículos activos.
   - Las emisiones de CO2 de cada vehículo (mg/s).

3. Los datos obtenidos se almacenan en un archivo CSV llamado:
   datos_simulacion_co2.csv

4. La simulación se ejecuta hasta que no quedan vehículos en el mapa y luego
   se cierra correctamente la conexión TraCI.

5. A partir del archivo CSV generado se calculan:
   - Emisiones promedio de CO2 por vehículo.
   - Emisión promedio general de la simulación.
   - Intervalo de confianza del 95% para la emisión promedio general.

6. Se generan dos gráficas en formato PNG:
   - CO2 promedio por vehículo.
   - CO2 promedio general con intervalo de confianza del 95%.


RESULTADOS

- Archivo CSV con las emisiones de CO2 por vehículo y por tiempo.
- Gráficas que permiten analizar visualmente las emisiones generadas.
- Valor promedio general de emisiones de CO2 de la simulación.


CONCLUSIONES

- TraCI permite obtener información ambiental detallada de la simulación
  en tiempo real.
- El cálculo de emisiones de CO2 es clave para evaluar el impacto ambiental
  del tráfico urbano.
- El uso de scripts en Python facilita el análisis reproducible y automatizado.
- Esta práctica es una base sólida para estudios avanzados de movilidad
  sostenible y evaluación ambiental.


SCRIPT UTILIZADO

- traci_co2.py (versionado en el repositorio del proyecto)

