import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros
fs = 10000 # Hz (frecuencia de muestreo)
T = 1.0  # esto será 1 segundo de duración de la señal
# pd: fs debe ser mucho mayor que la frecuencia de la señal para evitar aliasing
t = np.linspace(0, T, int(fs*T), endpoint=False)
f = 5  # Hz (5 ciclos en 1 s)

# Versiones periódicas (clásicas, en [-1,1])
cuadrada  = signal.square(2*np.pi*f*t)                 
sierra = signal.sawtooth(2*np.pi*f*t)               
tri = signal.sawtooth(2*np.pi*f*t, width=0.5)    
seno = np.sin(2*np.pi*f*t)                       

#normalizamos a [0,1] para que queden no negativas
cuadrada_n  = (cuadrada+1)/2
sierra_n = (sierra + 1)/2
tri_n = (tri+1)/2
# la seno puede quedar en [-1,1] o también (seno+1)/2

# Grfica de las versiones periódicas normalizadas
plt.figure(figsize=(10,8))
plt.subplot(4,1,1); plt.plot(t, cuadrada_n);  plt.title('Cuadrada (0–1)');   plt.ylim(-0.2,1.2); plt.grid(True)
plt.subplot(4,1,2); plt.plot(t, sierra_n); plt.title('Sierra (0–1)');     plt.ylim(-0.2,1.2); plt.grid(True)
plt.subplot(4,1,3); plt.plot(t, tri_n); plt.title('Triangular (0–1)'); plt.ylim(-0.2,1.2); plt.grid(True)
plt.subplot(4,1,4); plt.plot(t, seno);  plt.title('Senoidal');  plt.ylim(-1.2,1.2); plt.grid(True)
plt.tight_layout(); plt.show()
