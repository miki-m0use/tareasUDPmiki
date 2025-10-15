import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros
fs = 1000
dt = 1/fs
T_total = 3.0
t = np.arange(0, T_total, dt)
f = 5  # Hz


sierra = signal.sawtooth(2*np.pi*f*t)    # [-1,1]
sierra_n = (sierra+1)/2                  # [0,1]  <<— igual que en Paso 1
x = sierra_n


u = lambda x: np.where(x >= 0, 1, 0)


h = np.exp(t) * (u(t) - u(t - 1))

# Corrimiento (reconstruye h con (t - tau))
tau = 2  # segundos
h_tau = np.exp((t - tau)) * (u(t - tau) - u(t - tau - 1))  # <- mismo patrón que h, pero con (t - tau)

# Convoluciones
y     = np.convolve(x, h,     mode='full') * dt
y_tau = np.convolve(x, h_tau, mode='full') * dt
t_y   = np.arange(t[0]+t[0], t[-1]+t[-1] + dt, dt)[:len(y)]

# Gráficas Generales
plt.figure(figsize=(11,7))
plt.subplot(3,1,1); plt.plot(t, x);              plt.title('x(t): sierra 0–1'); plt.grid(True)
plt.subplot(3,1,2); plt.plot(t, h, label='h');   plt.plot(t, h_tau, '--', label='h_τ=h(t-τ)'); plt.legend(); plt.grid(True)
plt.subplot(3,1,3); plt.plot(t_y, y, label='y'); plt.plot(t_y, y_tau, '--', label='y_τ');      plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()