import traci
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# =========================
# RUTAS
# =========================
SUMO_CFG = "../../practica_02_osm_basico/simulacion_osm.sumocfg"
OUTPUT_DIR = "../resultados"
CSV_PATH = os.path.join(OUTPUT_DIR, "datos_simulacion_co2.csv")
PNG_CO2_VEH = os.path.join(OUTPUT_DIR, "co2_promedio_por_vehiculo.png")
PNG_CO2_GEN = os.path.join(OUTPUT_DIR, "co2_promedio_general.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# INICIAR SUMO CON TRACI
# =========================
traci.start([
    "sumo",
    "-c",
    SUMO_CFG
])

# =========================
# RECOLECCIÓN DE DATOS
# =========================
with open(CSV_PATH, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time", "VehicleID", "CO2"])

    while traci.simulation.getMinExpectedNumber() > 0:
        tiempo = traci.simulation.getTime()  # segundos

        for veh_id in traci.vehicle.getIDList():
            co2 = traci.vehicle.getCO2Emission(veh_id)
            writer.writerow([tiempo, veh_id, co2])

        traci.simulationStep()

traci.close()

# =========================
# ANÁLISIS DE DATOS
# =========================
datos = pd.read_csv(CSV_PATH)

# CO2 promedio por vehículo
co2_promedio_por_vehiculo = datos.groupby("VehicleID")["CO2"].mean()

# CO2 promedio general
co2_promedio_general = datos["CO2"].mean()

# Intervalo de confianza 95%
intervalo_confianza = stats.sem(datos["CO2"]) * 1.96

print(f"\nCO2 promedio general: {co2_promedio_general:.2f} mg/s")

# =========================
# GRÁFICAS
# =========================

# --- Gráfica 1: CO2 promedio por vehículo ---
plt.figure(figsize=(12, 6))
sns.barplot(
    x=co2_promedio_por_vehiculo.index,
    y=co2_promedio_por_vehiculo.values
)
plt.title("CO2 promedio por vehículo")
plt.xlabel("ID del vehículo")
plt.ylabel("CO2 promedio (mg/s)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(PNG_CO2_VEH)
plt.close()

# --- Gráfica 2: CO2 promedio general + IC 95% ---
plt.figure(figsize=(6, 6))
plt.bar(
    ["CO2 promedio"],
    [co2_promedio_general],
    yerr=[intervalo_confianza],
    capsize=8
)
plt.title("CO2 promedio general con IC 95%")
plt.ylabel("CO2 promedio (mg/s)")
plt.tight_layout()
plt.savefig(PNG_CO2_GEN)
plt.close()

print("\nArchivos generados:")
print(f"- {CSV_PATH}")
print(f"- {PNG_CO2_VEH}")
print(f"- {PNG_CO2_GEN}\n")

