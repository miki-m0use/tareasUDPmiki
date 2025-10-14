import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros generales
fs = 1000      # Frecuencia de muestreo (Hz)
T = 1          # Duración total de la simulación (s)
t = np.linspace(0, T, int(fs*T), endpoint=False)


# --- 1. Señal Cuadrada: un solo pulso ---
cuadrada = np.zeros_like(t)
cuadrada[(t >= 0.2) & (t < 0.4)] = 1  # pulso entre 0.2s y 0.4s

# --- 2. Señal Diente de Sierra: un solo pulso ---
sierra = np.zeros_like(t)
# parte ascendente lineal (un solo ciclo)
mask = (t >= 0.2) & (t < 0.4)
sierra[mask] = (t[mask] - 0.2) / (0.4 - 0.2)  # de -1 a +1

# --- 3. Señal Triangular: un solo pulso ---
triangular = np.zeros_like(t)
mask1 = (t >= 0.2) & (t < 0.3)
mask2 = (t >= 0.3) & (t < 0.4)
triangular[mask1] = (t[mask1] - 0.2) / (0.1)   # sube de -1 a +1
triangular[mask2] = 1 - (t[mask2] - 0.3) / (0.1)   # baja de +1 a -1

# --- 4. Señal Senoidal: un solo ciclo completo ---
f = 2  # Hz
seno = np.sin(2 * np.pi * f * t)  # un ciclo entero dentro de [0,1s]

# --- Gráficos ---
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1) # el subplot especifica la posición en la cuadrícula, sus numeros son (nfilas, ncolumnas, índice)
plt.plot(t, cuadrada, color='r')
plt.title('Señal Cuadrada (1 solo pulso)')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, sierra, color='g')
plt.title('Señal Diente de Sierra (1 solo pulso)')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, triangular, color='b')
plt.title('Señal Triangular (1 solo pulso)')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t, seno, color='m')
plt.title('Señal Senoidal (1 ciclo completo)')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.tight_layout()
plt.show()

