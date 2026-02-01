import traci

# Iniciar la conexión TraCI con SUMO
traci.start([
    "sumo",
    "-c",
    "../practica_02_osm_basico/simulacion_osm.sumocfg"
])

# Set para almacenar IDs únicos de vehículos
vehiculos_unicos = set()

# Ejecutar la simulación
while traci.simulation.getMinExpectedNumber() > 0:
    for veh_id in traci.vehicle.getIDList():
        vehiculos_unicos.add(veh_id)

    traci.simulationStep()

# Cerrar TraCI
traci.close()

print(f"\nEn el mapa han circulado un total de {len(vehiculos_unicos)} vehículos\n")

