import traci

traci.start([
    "sumo",
    "-c",
    "../../practica_02_osm_basico/simulacion_osm.sumocfg"
])

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

traci.close()
