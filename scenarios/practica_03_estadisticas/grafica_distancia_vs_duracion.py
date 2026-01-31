import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tripinfo.csv")

plt.figure(figsize=(6,6))
plt.scatter(
    df["tripinfo_routeLength"],
    df["tripinfo_duration"],
    s=10
)
plt.xlabel("Distancia recorrida (m)")
plt.ylabel("Duración del viaje (s)")
plt.title("Distancia vs duración del viaje")
plt.tight_layout()
plt.show()
