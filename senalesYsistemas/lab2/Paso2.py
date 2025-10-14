import numpy as np
import matplotlib.pyplot as plt

# Definimos el vector de tiempo
t = np.linspace(-1, 3, 1000)  # De -1 a 3 segundos
u = lambda x: np.where(x >= 0, 1, 0)  # Escalón unitario discreto

# 1. Exponencial decreciente (un tramo): e^(-t)[u(t) - u(t-1)]
x_exp_dec = np.exp(-t) * (u(t) - u(t - 1))

# 2. Exponencial creciente (un tramo): e^(t)[u(t) - u(t-1)]
x_exp_cre = np.exp(t) * (u(t) - u(t - 1))

# 3. Impulso: δ(t) ≈ una aproximación numérica (1 en t=0)
x_delta = np.where(np.isclose(t, 0, atol=2e-3), 1, 0)

# 4. Escalón: u(t)
x_escalon = u(t)

# 5. Sinc: sin(x)/x (usamos np.sinc que ya normaliza como sin(pi x)/(pi x))
x_sinc = np.sinc(t)

# --- Graficar ---
fig, axs = plt.subplots(5, 1, figsize=(8, 10))

axs[0].plot(t, x_exp_dec); axs[0].set_title("Exponencial Decreciente")
axs[1].plot(t, x_exp_cre); axs[1].set_title("Exponencial Creciente")
axs[2].stem(t, x_delta, basefmt=" ", markerfmt='ro', linefmt='r-')
axs[2].set_title("Impulso δ(t) (aproximación)")
axs[3].plot(t, x_escalon); axs[3].set_title("Escalón unitario u(t)")
axs[4].plot(t, x_sinc); axs[4].set_title("Función sinc(x)/x")

for ax in axs:
    ax.grid(True)
plt.tight_layout()
plt.show()
