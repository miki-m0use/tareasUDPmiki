import numpy as np
import matplotlib.pyplot as plt

# ===== Escala de tiempo =====
# 1 unidad = 100 ms
units_to_ms = 100.0               # factor de conversión
dt_u = 0.001                      # paso en "unidades" (0.001 u = 0.1 ms)
t_u = np.arange(-1.0, 10.0, dt_u) # tiempo en unidades (amplio para ver todo)

# Para mostrar en milisegundos:
t_ms  = t_u * units_to_ms

# Escalón unitario
u = lambda x: np.where(x >= 0, 1.0, 0.0)

# ===== Señales =====
# (¡Exactamente tu fórmula!)
x_exp_dec = np.exp(-t_u) * (u(t_u) - u(t_u - 1))   # vive en [0,1] unidades -> [0,100] ms

# Pulso cuadrado en [200,400] ms -> [2,4] unidades
h = np.zeros_like(t_u)
h[(t_u >= 2.0) & (t_u < 4.0)] = 1.0

# ===== Convolución continua aproximada =====
# Ojo: para aproximar la integral, multiplicamos por dt en SEGUNDOS.
# 1 unidad = 0.1 s (100 ms)
dt_s = dt_u * 0.1
y = np.convolve(x_exp_dec, h, mode='full') * dt_s

# Eje de tiempo de la salida (en unidades y en ms)
t_y_u  = np.arange(t_u[0] + t_u[0], t_u[-1] + t_u[-1] + dt_u, dt_u)[:len(y)]
t_y_ms = t_y_u * units_to_ms

# ===== Gráficas =====
plt.figure(figsize=(10, 8))

plt.subplot(3,1,1)
plt.plot(t_ms, x_exp_dec)
plt.title('x(t): e^{-t} en [0,100] ms (manteniendo x=exp(-t)[u(t)-u(t-1)])')
plt.ylabel('Amplitud'); plt.grid(True)
plt.xlim(-50, 500)
plt.axvline(0,  color='k', linestyle=':', linewidth=0.8)
plt.axvline(100, color='k', linestyle=':', linewidth=0.8)

plt.subplot(3,1,2)
plt.plot(t_ms, h)
plt.title('h(t): pulso cuadrado en [200, 400] ms')
plt.ylabel('Amplitud'); plt.grid(True)
plt.xlim(-50, 500)
plt.axvline(200, color='k', linestyle=':', linewidth=0.8)
plt.axvline(400, color='k', linestyle=':', linewidth=0.8)

plt.subplot(3,1,3)
plt.plot(t_y_ms, y)
plt.title('y(t) = x(t) * h(t)  (Convolución)')
plt.xlabel('Tiempo [ms]'); plt.ylabel('Amplitud'); plt.grid(True)
plt.xlim(0, 1000)  # el soporte va de 200 a 500 ms (aprox), pero muestro más
plt.tight_layout()
plt.show()
