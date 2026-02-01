import traci
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear directorio de resultados si no existe
os.makedirs("../resultados", exist_ok=True)

# Iniciar conexión TraCI
traci.start([
    "sumo",
    "-c",
    "../../practica_02_osm_basico/simulacion_osm.sumocfg"
])

csv_file = "../resultados/datos_velocidad.csv"

# Crear archivo CSV
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time", "VehicleID", "Speed"])

    # Ejecutar simulación
    while traci.simulation.getMinExpectedNumber() > 0:
        tiempo = tiempo = traci.simulation.getTime()

        for veh_id in traci.vehicle.getIDList():
            velocidad = traci.vehicle.getSpeed(veh_id)
            writer.writerow([tiempo, veh_id, velocidad])

        traci.simulationStep()

# Cerrar TraCI
traci.close()

# =====================
# ANÁLISIS DE DATOS
# =====================

datos = pd.read_csv(csv_file)

# Velocidad promedio por vehículo
velocidad_por_vehiculo = datos.groupby("VehicleID")["Speed"].mean()

# Velocidad promedio general
velocidad_promedio_general = datos["Speed"].mean()

print(f"\nVelocidad promedio general: {velocidad_promedio_general:.2f} m/s\n")

# =====================
# GRÁFICAS
# =====================

# Gráfica 1: Velocidad promedio por vehículo
plt.figure(figsize=(10, 5))
velocidad_por_vehiculo.plot(kind="bar")
plt.title("Velocidad promedio por vehículo")
plt.xlabel("ID del vehículo")
plt.ylabel("Velocidad promedio (m/s)")
plt.tight_layout()
plt.savefig("../resultados/velocidad_promedio_por_vehiculo.png")
plt.close()

# Gráfica 2: Velocidad promedio general
plt.figure(figsize=(6, 4))
plt.bar(["Promedio"], [velocidad_promedio_general])
plt.ylabel("Velocidad promedio (m/s)")
plt.title("Velocidad promedio general")
plt.tight_layout()
plt.savefig("../resultados/velocidad_promedio_general.png")
plt.close()

