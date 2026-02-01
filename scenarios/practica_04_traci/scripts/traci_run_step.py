import traci

traci.start([
    "sumo",
    "-c",
    "../../practica_02_osm_basico/simulacion_osm.sumocfg"
])

step = 0
MAX_STEPS = 4000

while step < MAX_STEPS:
    traci.simulationStep()
    step += 1

print("Simulación finalizada en el paso:", step)
print("Tiempo simulado:", traci.simulation.getTime())

traci.close()

