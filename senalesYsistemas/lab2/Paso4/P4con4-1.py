import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# === Parámetros (mismo estilo), solo más duración para evitar bordes ===
fs = 1000
dt = 1/fs
T_total = 3.0                      # > 1 s para ver régimen
t = np.arange(0, T_total, dt)
f = 5                              # Hz (mismo que antes)

# === Señal periódica cuadrada como en tus pasos (0..1) ===
sierra = signal.sawtooth(2*np.pi*f*t)    # [-1,1]
sierra_n = (sierra+1)/2                  # [0,1]  <<— igual que en Paso 1

# === Escalón unitario como en tus pasos ===
u = lambda x: np.where(x >= 0, 1, 0)


x_exp_dec = np.exp(t) * (u(t) - u(t - 1))   # e^{t}[u(t)-u(t-1)]

#Escalamiento de la respuesta al impulso
A = 10
x_exp_dec = A * x_exp_dec  # este seria como un "h"

# === Convolución continua aproximada ===
y = np.convolve(sierra_n, x_exp_dec, mode='full') * dt
t_y = np.arange(t[0]+t[0], t[-1]+t[-1]+dt, dt)[:len(y)]

#  Gráficos generales
plt.figure(figsize=(10,7))
plt.subplot(3,1,1); plt.plot(t, sierra_n);      plt.title('x(t): sierra periodica (0–1)');       plt.grid(True)
plt.subplot(3,1,2); plt.plot(t, x_exp_dec); plt.title('h(t): e^{-t}[u(t)-u(t-1)]');            plt.grid(True)
plt.subplot(3,1,3); plt.plot(t_y, y);       plt.title('y(t) = x * h');    plt.grid(True)
plt.tight_layout(); plt.show()