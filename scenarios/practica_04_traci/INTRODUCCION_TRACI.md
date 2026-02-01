# Práctica 1.7 – Introducción a TraCI

## Objetivo
Introducir la librería TraCI para Python, comprender su funcionamiento bajo una
arquitectura cliente/servidor y verificar la correcta configuración de la
variable de entorno `SUMO_HOME`, necesaria para la comunicación entre Python y
el simulador SUMO.

---

## 1. ¿Qué es TraCI?

TraCI (Traffic Control Interface) es una interfaz que permite acceder y controlar
una simulación de tráfico en SUMO mientras esta se encuentra en ejecución. A
través de TraCI es posible recuperar valores de los objetos simulados y modificar
su comportamiento de forma dinámica.

A diferencia de una simulación estática, TraCI permite implementar control en
tiempo real, lo cual es fundamental para el desarrollo de sistemas inteligentes
de transporte (ITS).

---

## 2. Arquitectura cliente–servidor

TraCI utiliza una arquitectura cliente/servidor basada en TCP:

- SUMO actúa como servidor
- La aplicación externa (Python) actúa como cliente

Cuando SUMO se ejecuta en modo TraCI:
- Prepara la simulación
- Espera conexiones externas
- No avanza la simulación hasta recibir órdenes del cliente

El cliente controla explícitamente cada paso de simulación, lo que permite una
interacción precisa y controlada.

---

## 3. Control del tiempo de simulación

En TraCI, el avance del tiempo no es automático. El cliente debe enviar el
comando de paso de simulación (`simulationStep`) para que SUMO avance.

La simulación finaliza únicamente cuando el cliente cierra la conexión, no
cuando se alcanza el tiempo final definido en el archivo `.sumocfg`.

---

## 4. Capacidades de TraCI

Mediante TraCI es posible:

### Recuperar valores
- Información de vehículos (velocidad, posición, emisiones)
- Detectores y salidas
- Red vial
- Infraestructura (semáforos)
- Variables ambientales

### Modificar el estado
- Cambiar velocidad y rutas
- Detener o reanudar vehículos
- Controlar semáforos
- Modificar parámetros de la red

### Suscripciones
- Obtener datos automáticamente en cada paso de simulación
- Optimizar el acceso a información en tiempo real

---

## 5. Importancia de la variable de entorno `SUMO_HOME`

La variable de entorno `SUMO_HOME` indica la ubicación de la instalación de SUMO
y es esencial para que Python pueda acceder correctamente a:

- La librería `traci`
- La librería `sumolib`
- Los scripts oficiales ubicados en `tools/`

Una configuración incorrecta de esta variable impide el uso adecuado de TraCI.

---

## 6. Verificación de la variable de entorno

Para verificar que `SUMO_HOME` esté correctamente definida y que la librería
TraCI sea accesible desde Python, se ejecutó un script llamado traci_check.py de comprobación que: 

- Verifica la existencia de la variable de entorno
- Muestra su valor
- Indica las rutas utilizadas por Python
- Muestra la ubicación de la librería TraCI cargada

Esta verificación confirma que el entorno está listo para desarrollar
aplicaciones basadas en TraCI.

---

## 7. Conclusión

TraCI constituye una herramienta fundamental para el control dinámico de
simulaciones de tráfico en SUMO. Su correcta configuración, junto con la
verificación de la variable `SUMO_HOME`, permite desarrollar aplicaciones que
interactúan con la simulación en tiempo real, habilitando el análisis avanzado y
el control inteligente del tráfico vehicular.
