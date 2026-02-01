import traci
import csv

# -------------------------------
# CONFIGURACIÓN
# -------------------------------

SUMOCFG_PATH = "../../practica_02_osm_basico/simulacion_osm.sumocfg"
EDGE_CONGESTION = "567060342#1"
EDGE_ALTERNATIVO = "1053072563"
UMBRAL_VELOCIDAD = 10.0  # m/s
CSV_SALIDA = "datos_change_trayectoria.csv"

# -------------------------------
# INICIAR SUMO + TRACI
# -------------------------------

traci.start([
    "sumo",          # cambiar por "sumo-gui" si quieres ver la simulación
    "-c",
    SUMOCFG_PATH
])

# Conjunto para no redirigir el mismo vehículo varias veces
vehiculos_redirigidos = set()

# -------------------------------
# ARCHIVO CSV
# -------------------------------

with open(CSV_SALIDA, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time", "VehicleID", "Speed_mps", "EdgeActual", "Redirigido"])

    # -------------------------------
    # BUCLE DE SIMULACIÓN
    # -------------------------------
    while traci.simulation.getMinExpectedNumber() > 0:
        tiempo = traci.simulation.getTime()  # segundos

        for veh_id in traci.vehicle.getIDList():
            speed = traci.vehicle.getSpeed(veh_id)
            edge_actual = traci.vehicle.getRoadID(veh_id)

            redirigido = "NO"

            # Lógica de congestión
            if (
                edge_actual == EDGE_CONGESTION
                and speed < UMBRAL_VELOCIDAD
                and veh_id not in vehiculos_redirigidos
            ):
                traci.vehicle.changeTarget(veh_id, EDGE_ALTERNATIVO)
                vehiculos_redirigidos.add(veh_id)
                redirigido = "SI"

                print(
                    f"🚦 Congestión detectada | Vehículo {veh_id} "
                    f"redirigido a {EDGE_ALTERNATIVO}"
                )

            writer.writerow([
                tiempo,
                veh_id,
                round(speed, 2),
                edge_actual,
                redirigido
            ])

        traci.simulationStep()

# -------------------------------
# CERRAR TRACI
# -------------------------------

traci.close()

print("\n✅ Simulación finalizada")
print(f"📁 Archivo generado: {CSV_SALIDA}")
print(f"🔁 Vehículos redirigidos: {len(vehiculos_redirigidos)}\n")

