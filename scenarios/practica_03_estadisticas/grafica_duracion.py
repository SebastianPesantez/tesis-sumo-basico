import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tripinfo.csv")

plt.figure(figsize=(8,4))
plt.hist(df["tripinfo_duration"], bins=30)
plt.xlabel("Duración del viaje (s)")
plt.ylabel("Número de vehículos")
plt.title("Distribución de la duración de viajes")
plt.tight_layout()
plt.show()
