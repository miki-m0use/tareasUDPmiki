import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros
fs = 1000
T = 1.0
t = np.linspace(0, T, int(fs*T), endpoint=False)
f = 5  # Hz (5 ciclos en 1 s)

# Versiones periódicas (clásicas, en [-1,1])
sq  = signal.square(2*np.pi*f*t)                 # cuadrada periódica
saw = signal.sawtooth(2*np.pi*f*t)               # diente de sierra periódico
tri = signal.sawtooth(2*np.pi*f*t, width=0.5)    # triangular periódica
sinv = np.sin(2*np.pi*f*t)                       # senoidal periódica

# Si las quieres no negativas: normaliza a [0,1]
sq_n  = (sq+1)/2
saw_n = (saw+1)/2
tri_n = (tri+1)/2
# la seno puede quedar en [-1,1] o también (sinv+1)/2 si te lo exigen

# Gráfica de las versiones periódicas normalizadas
plt.figure(figsize=(10,8))
plt.subplot(4,1,1); plt.plot(t, sq_n);  plt.title('Cuadrada (0–1)');   plt.ylim(-0.2,1.2); plt.grid(True)
plt.subplot(4,1,2); plt.plot(t, saw_n); plt.title('Sierra (0–1)');     plt.ylim(-0.2,1.2); plt.grid(True)
plt.subplot(4,1,3); plt.plot(t, tri_n); plt.title('Triangular (0–1)'); plt.ylim(-0.2,1.2); plt.grid(True)
plt.subplot(4,1,4); plt.plot(t, sinv);  plt.title('Senoidal (-1–1)');  plt.ylim(-1.2,1.2); plt.grid(True)
plt.tight_layout(); plt.show()
