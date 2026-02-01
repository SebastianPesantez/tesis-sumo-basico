Práctica 1.9 – Simulación TraCI/SUMO: Contador de Vehículos

Objetivos
- Integrar la interfaz TraCI con SUMO.
- Ejecutar una simulación de tráfico vehicular controlada desde Python.
- Contar el número total de vehículos que circularon en el mapa durante la simulación.

Introducción
El análisis del tráfico urbano requiere no solo observar el movimiento de los vehículos,
sino también cuantificar métricas clave como el número total de vehículos que circulan
en una red vial.

SUMO, junto con la interfaz TraCI, permite acceder en tiempo real a los elementos de la
simulación, lo que facilita la recopilación de información dinámica como identificadores
de vehículos, velocidades y posiciones.

En esta práctica se utiliza TraCI para contar el número total de vehículos que circularon
por el mapa durante toda la simulación, sin depender de supuestos sobre la nomenclatura
de los identificadores generados automáticamente por SUMO.

Estructura del directorio
La práctica se desarrolló en el siguiente directorio del repositorio:

scenarios/practica_05_traci_contador/

Contenido principal:
- traci_cont_veh.py : Script TraCI para contar vehículos.
- Archivo de configuración reutilizado:
  practica_02_osm_basico/simulacion_osm.sumocfg

Metodología

1. Conexión TraCI–SUMO
La simulación se inicia desde Python utilizando la librería traci, ejecutando SUMO
en modo servidor mediante el archivo de configuración .sumocfg previamente creado
en la práctica OSM.

La simulación queda bajo control total de TraCI, el cual avanza el tiempo paso a paso.

2. Ejecución de la simulación
La simulación se ejecuta mientras existan vehículos activos o esperados en la red,
utilizando el criterio:

traci.simulation.getMinExpectedNumber() > 0

Esto garantiza que la simulación finaliza únicamente cuando todos los vehículos han
completado su recorrido.

3. Conteo de vehículos
Durante cada paso de simulación:
- Se obtiene la lista de vehículos presentes mediante:
  traci.vehicle.getIDList()
- Los identificadores se almacenan en una estructura de tipo conjunto (set) para:
  - Evitar duplicados.
  - Contabilizar cada vehículo una sola vez, independientemente del tiempo que
    permanezca en la red.

Este enfoque es robusto y no depende del formato interno de los IDs generados por SUMO.

4. Finalización de la simulación
Una vez que no quedan vehículos en la simulación:
- Se cierra correctamente la conexión TraCI.
- Se imprime el número total de vehículos únicos que circularon por el mapa.

Script utilizado
Nombre del script: traci_cont_veh.py
Lenguaje: Python
Interfaz: TraCI
Entrada: Archivo simulacion_osm.sumocfg
Salida: Conteo total de vehículos que circularon en la simulación

Resultado obtenido
Al ejecutar el script se obtiene una salida similar a:

En el mapa han circulado un total de N vehículos

Donde N corresponde al número real de vehículos insertados y simulados en la red,
coincidiendo con lo observado en la simulación gráfica de SUMO.

Conclusiones
- TraCI permite acceder de manera directa y precisa a los vehículos activos en una
  simulación SUMO.
- El uso de estructuras de datos adecuadas evita errores al contar vehículos múltiples
  veces.
- El conteo de vehículos mediante TraCI es más confiable que una inspección visual
  desde la interfaz gráfica.
- Esta práctica constituye la base para análisis más avanzados como conteo por zonas,
  intersecciones o intervalos de tiempo.

Observaciones
- No fue necesario modificar el archivo .sumocfg para esta práctica.
- El control del tiempo de simulación recae completamente en TraCI.
- No se deben realizar llamadas a TraCI después de cerrar la conexión.

Trabajo futuro
- Conteo de vehículos por intervalo de tiempo.
- Conteo por carril o intersección.
- Relación entre flujo vehicular y emisiones contaminantes.
