PRACTICA 1.10
SIMULACION DE TRAFICO VEHICULAR – TRACI / SUMO
CALCULO DE VELOCIDAD PROMEDIO


OBJETIVOS

- Integrar la interfaz TraCI con SUMO.
- Simular una red vehicular sobre SUMO utilizando scripts en Python.
- Calcular la velocidad promedio de los vehículos que circularon en el mapa.


INTRODUCCION

La simulación del tráfico urbano permite analizar el comportamiento de los
vehículos y evaluar el rendimiento de una red vial. TraCI (Traffic Control
Interface) proporciona acceso en tiempo real a los datos de la simulación
SUMO, permitiendo obtener información como la velocidad de los vehículos
en cada instante.

En esta práctica se utiliza TraCI para registrar las velocidades de los
vehículos durante la simulación y posteriormente calcular la velocidad
promedio por vehículo y la velocidad promedio general del sistema.


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

practica_06_traci_velocidad/
│
├── scripts/
│   └── traci_velocidad_promedio.py
│
└── resultados/
    ├── datos_simulacion_velocidad.csv
    ├── velocidad_promedio_por_vehiculo.png
    └── velocidad_promedio_general.png


PROCEDIMIENTO

1. Se inicia la comunicación entre SUMO y TraCI desde un script en Python,
   indicando el archivo de configuración .sumocfg de la simulación.

2. Durante cada paso de la simulación se obtienen:
   - El tiempo de simulación en segundos.
   - Los identificadores de los vehículos activos.
   - La velocidad instantánea de cada vehículo.

3. Los datos recolectados se almacenan en un archivo CSV llamado:
   datos_simulacion_velocidad.csv

4. La simulación se ejecuta hasta que no quedan vehículos en el mapa y
   posteriormente se cierra la conexión TraCI.

5. A partir del archivo CSV se calcula:
   - La velocidad promedio de cada vehículo.
   - La velocidad promedio general de toda la simulación.
   - El intervalo de confianza del 95% para la velocidad promedio general.

6. Se generan dos gráficas en formato PNG:
   - Velocidad promedio por vehículo.
   - Velocidad promedio general con intervalo de confianza del 95%.


RESULTADOS

- Archivo CSV con registros de velocidad por vehículo y tiempo.
- Gráficas que permiten visualizar el comportamiento promedio de las
  velocidades en la red.
- Valor numérico de la velocidad promedio general del sistema.


CONCLUSIONES

- TraCI permite acceder a la velocidad de los vehículos en tiempo real.
- El cálculo de la velocidad promedio es útil para evaluar el desempeño
  de una red vial.
- El análisis estadístico permite interpretar mejor el comportamiento
  global del tráfico.
- Esta práctica sienta las bases para estudios más avanzados de movilidad
  urbana y eficiencia del tráfico.


SCRIPT UTILIZADO

- traci_velocidad_promedio.py (versionado en el repositorio del proyecto)

